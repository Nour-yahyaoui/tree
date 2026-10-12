"""Tests for argument parsing and end-to-end CLI behaviour."""

from __future__ import annotations

import json
import os
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

from tests.support import TempTreeCase
from treepy.cli import build_parser, main


class ParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = build_parser()

    def test_defaults(self):
        args = self.parser.parse_args([])
        self.assertEqual(args.paths, ["."])
        self.assertEqual(args.sort, "name")
        self.assertEqual(args.color, "auto")
        self.assertIsNone(args.depth)
        self.assertFalse(args.json)

    def test_short_flags(self):
        args = self.parser.parse_args(["-L", "2", "-a", "-d", "-s", "-H", "-q"])
        self.assertEqual(args.depth, 2)
        self.assertTrue(args.all)
        self.assertTrue(args.dirs_only)
        self.assertTrue(args.size)
        self.assertTrue(args.human_readable)
        self.assertTrue(args.quiet)

    def test_multiple_paths(self):
        args = self.parser.parse_args(["src", "tests"])
        self.assertEqual(args.paths, ["src", "tests"])

    def test_exclude_is_repeatable(self):
        args = self.parser.parse_args(["-I", "*.pyc", "-I", "*.log"])
        self.assertEqual(args.exclude, ["*.pyc", "*.log"])

    def test_bad_sort_key_exits(self):
        with self.assertRaises(SystemExit):
            with redirect_stderr(StringIO()):
                self.parser.parse_args(["--sort", "colour"])


class CliTests(TempTreeCase):
    def run_cli(self, argv):
        out, err = StringIO(), StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_prints_a_tree(self):
        self.make("alpha.txt")
        code, out, _ = self.run_cli([self.root, "--color", "never"])
        self.assertEqual(code, 0)
        self.assertIn("alpha.txt", out)
        self.assertIn("1 directory, 1 file", out)

    def test_quiet_hides_the_summary(self):
        self.make("alpha.txt")
        _, out, _ = self.run_cli([self.root, "-q"])
        self.assertNotIn("directory", out)

    def test_depth_zero(self):
        self.make("sub/alpha.txt")
        _, out, _ = self.run_cli([self.root, "-L", "0"])
        self.assertNotIn("alpha.txt", out)

    def test_json_output_is_valid(self):
        self.make("sub/alpha.txt", "hello")
        code, out, _ = self.run_cli([self.root, "--json"])
        document = json.loads(out)
        self.assertEqual(code, 0)
        self.assertEqual(document["stats"]["files"], 1)
        self.assertEqual(document["stats"]["directories"], 2)

    def test_ascii_output(self):
        self.make("alpha.txt")
        _, out, _ = self.run_cli([self.root, "--ascii"])
        self.assertIn("`-- alpha.txt", out)

    def test_exclude_pattern(self):
        self.make("keep.txt")
        self.make("drop.log")
        _, out, _ = self.run_cli([self.root, "-I", "*.log"])
        self.assertIn("keep.txt", out)
        self.assertNotIn("drop.log", out)

    def test_include_pattern(self):
        self.make("keep.txt")
        self.make("drop.md")
        _, out, _ = self.run_cli([self.root, "-P", "*.txt"])
        self.assertIn("keep.txt", out)
        self.assertNotIn("drop.md", out)

    def test_gitignore_is_respected(self):
        self.make(".gitignore", "*.log\n")
        self.make("keep.txt")
        self.make("drop.log")
        _, out, _ = self.run_cli([self.root, "--gitignore"])
        self.assertNotIn("drop.log", out)

    def test_max_entries(self):
        for name in ("a.txt", "b.txt", "c.txt", "d.txt"):
            self.make(name)
        _, out, _ = self.run_cli([self.root, "--max-entries", "2"])
        self.assertEqual(out.count(".txt"), 2)

    def test_output_file(self):
        self.make("alpha.txt")
        destination = os.path.join(self.root, "out.txt")
        code, out, _ = self.run_cli([self.root, "-o", destination])
        self.assertEqual(code, 0)
        self.assertEqual(out, "")
        with open(destination, encoding="utf-8") as handle:
            self.assertIn("alpha.txt", handle.read())

    def test_missing_path_sets_exit_code(self):
        code, _, err = self.run_cli([os.path.join(self.root, "missing")])
        self.assertEqual(code, 1)
        self.assertIn("treepy:", err)

    def test_negative_depth_is_rejected(self):
        with self.assertRaises(SystemExit):
            with redirect_stderr(StringIO()):
                main([self.root, "-L", "-1"])

    def test_multiple_roots_are_printed(self):
        first = self.mkdir("first")
        second = self.mkdir("second")
        self.make("first/a.txt")
        self.make("second/b.txt")
        _, out, _ = self.run_cli([first, second])
        self.assertIn("a.txt", out)
        self.assertIn("b.txt", out)

    def test_version_flag(self):
        with self.assertRaises(SystemExit) as caught:
            with redirect_stdout(StringIO()):
                main(["--version"])
        self.assertEqual(caught.exception.code, 0)

    def test_du_shows_totals(self):
        self.make("sub/a.txt", "x" * 2048)
        _, out, _ = self.run_cli([self.root, "--du", "-H"])
        self.assertIn("[2.0K]", out)
