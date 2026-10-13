"""Tests for the gitignore-style pattern matcher."""

from __future__ import annotations

import os
import unittest

from tests.support import TempTreeCase
from treepy.ignore import IgnoreSet, Pattern, filter_tree, prune_tree
from treepy.node import Node, Stats


class PatternTests(unittest.TestCase):
    def test_blank_and_comment_lines_are_skipped(self):
        self.assertIsNone(Pattern.parse(""))
        self.assertIsNone(Pattern.parse("   "))
        self.assertIsNone(Pattern.parse("# a comment"))
        self.assertIsNone(Pattern.parse("!/"))

    def test_plain_name_matches_at_any_level(self):
        pattern = Pattern.parse("node_modules")
        self.assertTrue(pattern.matches("node_modules", True))
        self.assertTrue(pattern.matches("packages/web/node_modules", True))
        self.assertFalse(pattern.matches("node_modules.txt", False))

    def test_pattern_with_slash_is_anchored(self):
        anchored = Pattern.parse("src/generated")
        loose = Pattern.parse("generated")
        self.assertTrue(anchored.matches("src/generated", True))
        self.assertFalse(anchored.matches("lib/src/generated", True))
        self.assertTrue(loose.matches("lib/src/generated", True))

    def test_star_does_not_cross_slash(self):
        pattern = Pattern.parse("logs/*.log")
        self.assertTrue(pattern.matches("logs/app.log", False))
        self.assertFalse(pattern.matches("logs/old/app.log", False))

    def test_bare_glob_matches_at_any_level(self):
        pattern = Pattern.parse("*.log")
        self.assertTrue(pattern.matches("app.log", False))
        self.assertTrue(pattern.matches("logs/app.log", False))

    def test_double_star_crosses_slash(self):
        pattern = Pattern.parse("**/build")
        self.assertTrue(pattern.matches("build", True))
        self.assertTrue(pattern.matches("a/build", True))
        self.assertTrue(pattern.matches("a/b/c/build", True))

    def test_question_mark_matches_one_character(self):
        pattern = Pattern.parse("file?.txt")
        self.assertTrue(pattern.matches("file1.txt", False))
        self.assertFalse(pattern.matches("file12.txt", False))

    def test_character_class(self):
        pattern = Pattern.parse("v[0-9].py")
        self.assertTrue(pattern.matches("v1.py", False))
        self.assertFalse(pattern.matches("vx.py", False))

    def test_directory_only_pattern_skips_files(self):
        pattern = Pattern.parse("cache/")
        self.assertTrue(pattern.matches("cache", True))
        self.assertFalse(pattern.matches("cache", False))

    def test_unclosed_bracket_is_literal(self):
        pattern = Pattern.parse("weird[.txt")
        self.assertTrue(pattern.matches("weird[.txt", False))


class IgnoreSetTests(TempTreeCase):
    def test_negation_restores_a_file(self):
        ignore = IgnoreSet.from_lines(["*.log", "!keep.log"])
        self.assertTrue(ignore.matches("debug.log", False))
        self.assertFalse(ignore.matches("keep.log", False))

    def test_last_matching_pattern_wins(self):
        ignore = IgnoreSet.from_lines(["!*.log", "*.log"])
        self.assertTrue(ignore.matches("a.log", False))

    def test_empty_set_is_falsey(self):
        empty = IgnoreSet.from_lines(["", "# nothing"])
        self.assertFalse(empty)
        self.assertEqual(len(empty), 0)

    def test_from_file_missing_file_is_empty(self):
        ignore = IgnoreSet.from_file(os.path.join(self.root, "nope"))
        self.assertEqual(len(ignore), 0)

    def test_from_file_reads_patterns(self):
        path = self.make(".gitignore", "*.pyc\n__pycache__/\n")
        ignore = IgnoreSet.from_file(path)
        self.assertEqual(len(ignore), 2)
        self.assertTrue(ignore.matches("a.pyc", False))

    def test_from_patterns_accepts_cli_globs(self):
        ignore = IgnoreSet.from_patterns(["*.tmp", "build/"])
        self.assertTrue(ignore.matches("x.tmp", False))
        self.assertTrue(ignore.matches("build", True))

    def test_merge_keeps_order(self):
        first = IgnoreSet.from_lines(["*.log"])
        second = IgnoreSet.from_lines(["!keep.log"])
        merged = first.merge(second)
        self.assertFalse(merged.matches("keep.log", False))


class FilterTreeTests(unittest.TestCase):
    def build(self) -> Node:
        root = Node(name="root", path="/root", is_dir=True)
        alpha = root.add(Node(name="alpha.txt", path="/root/alpha.txt", is_dir=False, relative="alpha.txt"))
        sub = root.add(Node(name="sub", path="/root/sub", is_dir=True, relative="sub"))
        sub.add(Node(name="beta.py", path="/root/sub/beta.py", is_dir=False, relative="sub/beta.py"))
        sub.add(Node(name="gamma.txt", path="/root/sub/gamma.txt", is_dir=False, relative="sub/gamma.txt"))
        del alpha
        return root

    def test_filter_keeps_matching_files_and_their_directories(self):
        root = self.build()
        kept = filter_tree(root, Pattern.parse("*.txt"))
        self.assertEqual([c.name for c in kept.children], ["alpha.txt", "sub"])
        self.assertEqual([c.name for c in kept.children[1].children], ["gamma.txt"])

    def test_filter_prunes_directories_without_survivors(self):
        root = self.build()
        kept = filter_tree(root, Pattern.parse("beta.py"))
        self.assertEqual([c.name for c in kept.children], ["sub"])
        self.assertEqual([c.name for c in kept.children[0].children], ["beta.py"])

    def test_filter_updates_stats(self):
        root = self.build()
        stats = Stats(dirs=2, files=3, total_bytes=30)
        filter_tree(root, Pattern.parse("*.txt"), stats)
        self.assertEqual(stats.files, 2)
        self.assertEqual(stats.dirs, 2)

    def test_prune_tree_trims_wide_directories(self):
        root = Node(name="root", path="/root", is_dir=True)
        for index in range(6):
            root.add(Node(name=f"f{index}", path=f"/root/f{index}", is_dir=False))
        prune_tree(root, 3)
        self.assertEqual(len(root.children), 3)

    def test_prune_tree_rejects_zero(self):
        root = Node(name="root", path="/root", is_dir=True)
        with self.assertRaises(ValueError):
            prune_tree(root, 0)
