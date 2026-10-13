"""Tests for the text and JSON renderers."""

from __future__ import annotations

import json
import unittest

from tests.support import TempTreeCase
from treepy.node import Node, Stats
from treepy.render import RenderOptions, human_size, node_to_dict, render_json, render_text
from treepy.style import Style, build_style, plain_style
from treepy.walker import WalkOptions, walk


class HumanSizeTests(unittest.TestCase):
    def test_bytes(self):
        self.assertEqual(human_size(0), "0B")
        self.assertEqual(human_size(999), "999B")

    def test_kilobytes(self):
        self.assertEqual(human_size(1024), "1.0K")
        self.assertEqual(human_size(1536), "1.5K")

    def test_megabytes_and_beyond(self):
        self.assertEqual(human_size(1024 ** 2), "1.0M")
        self.assertEqual(human_size(1024 ** 3), "1.0G")

    def test_huge_values_stop_at_petabytes(self):
        self.assertIn("P", human_size(1024 ** 6))


class TextRendererTests(TempTreeCase):
    def test_unicode_glyphs_by_default(self):
        self.make("a.txt")
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(root, RenderOptions(style=plain_style()))
        self.assertIn("└── a.txt", text)

    def test_ascii_glyphs(self):
        self.make("a.txt")
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(root, RenderOptions(ascii_only=True, style=plain_style()))
        self.assertIn("`-- a.txt", text)

    def test_summary_counts_directories_and_files(self):
        self.make("a.txt")
        self.make("sub/b.txt")
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(root, RenderOptions(style=plain_style()))
        self.assertIn("2 directories, 2 files", text)

    def test_singular_forms(self):
        self.make("only.txt")
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(root, RenderOptions(style=plain_style()))
        self.assertIn("1 directory, 1 file", text)

    def test_quiet_hides_the_summary(self):
        self.make("a.txt")
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(root, RenderOptions(style=plain_style(), show_summary=False))
        self.assertNotIn("directories", text)

    def test_sizes_are_shown_in_brackets(self):
        self.make("a.txt", "1234")
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(root, RenderOptions(style=plain_style(), show_sizes=True))
        self.assertIn("[4]", text)

    def test_human_sizes_when_asked(self):
        self.make("a.txt", "x" * 2048)
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(
            root, RenderOptions(style=plain_style(), show_sizes=True, human=True)
        )
        self.assertIn("[2.0K]", text)

    def test_directory_totals_with_du(self):
        self.make("sub/deep/a.txt", "x" * 300)
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(
            root,
            RenderOptions(style=plain_style(), show_sizes=True, dir_sizes=True, human=True),
        )
        self.assertIn("sub [300B]", text)

    def test_symlink_targets_are_printed(self):
        import os

        self.make("real.txt", "x")
        if not hasattr(os, "symlink"):
            self.skipTest("no symlink support")
        os.symlink(os.path.join(self.root, "real.txt"), os.path.join(self.root, "alias.txt"))
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(root, RenderOptions(style=plain_style()))
        self.assertIn("alias.txt ->", text)

    def test_errors_can_be_hidden(self):
        node = Node(name="broken", path="/broken", is_dir=False, error="permission denied")
        node.relative = "broken"
        root = Node(name="root", path="/", is_dir=True)
        root.add(node)
        shown = render_text(root, RenderOptions(style=plain_style()))
        hidden = render_text(root, RenderOptions(style=plain_style(), show_errors=False))
        self.assertIn("permission denied", shown)
        self.assertNotIn("permission denied", hidden)

    def test_bytes_total_in_summary(self):
        self.make("a.txt", "12345")
        root = walk(self.root, WalkOptions(), Stats())
        text = render_text(
            root, RenderOptions(style=plain_style(), show_bytes_total=True)
        )
        self.assertIn("5 total", text)


class JsonRendererTests(TempTreeCase):
    def test_document_shape(self):
        self.make("sub/a.txt", "1234")
        stats = Stats()
        root = walk(self.root, WalkOptions(), stats)
        document = json.loads(render_json([root], stats))
        self.assertEqual(document["version"], 1)
        self.assertIn("stats", document)
        self.assertEqual(len(document["trees"]), 1)

    def test_nested_children_and_sizes(self):
        self.make("sub/a.txt", "1234")
        root = walk(self.root, WalkOptions(), Stats())
        payload = node_to_dict(root)
        sub = payload["children"][0]
        self.assertEqual(sub["type"], "directory")
        self.assertEqual(sub["children"][0]["size"], 4)

    def test_paths_are_relative_to_the_root(self):
        self.make("sub/a.txt")
        root = walk(self.root, WalkOptions(), Stats())
        payload = node_to_dict(root)
        self.assertEqual(payload["children"][0]["path"], "sub")

    def test_symlinks_carry_the_target(self):
        import os

        self.make("real.txt")
        if not hasattr(os, "symlink"):
            self.skipTest("no symlink support")
        os.symlink("real.txt", os.path.join(self.root, "link.txt"))
        root = walk(self.root, WalkOptions(), Stats())
        payload = node_to_dict(root)
        alias = [child for child in payload["children"] if child["name"] == "link.txt"][0]
        self.assertTrue(alias["symlink"])
        self.assertEqual(alias["target"], "real.txt")

    def test_json_is_parseable_and_ends_with_newline(self):
        self.make("a.txt")
        root = walk(self.root, WalkOptions(), Stats())
        text = render_json([root])
        self.assertTrue(text.endswith("\n"))
        json.loads(text)


class StyleTests(unittest.TestCase):
    def test_plain_style_never_paints(self):
        style = plain_style()
        self.assertEqual(style.directory("src"), "src")
        self.assertEqual(style.file("main.py"), "main.py")

    def test_enabled_style_uses_escape_sequences(self):
        style = Style(enabled=True)
        self.assertIn("\033[", style.directory("src"))
        self.assertTrue(style.directory("src").endswith("\033[0m"))

    def test_unknown_mode_is_rejected(self):
        with self.assertRaises(ValueError):
            build_style("sometimes")

    def test_never_mode_is_plain(self):
        self.assertFalse(build_style("never").enabled)

    def test_always_mode_is_enabled(self):
        self.assertTrue(build_style("always", stream=None).enabled)

    def test_auto_mode_without_a_tty_is_plain(self):
        class NotATty:
            def isatty(self):
                return False

        self.assertFalse(build_style("auto", stream=NotATty()).enabled)

    def test_executable_files_are_painted_differently(self):
        style = Style(enabled=True)
        self.assertNotEqual(style.file("run.sh", executable=True), style.file("run.sh"))

    def test_unknown_extensions_are_untouched(self):
        style = Style(enabled=True)
        self.assertEqual(style.file("mystery"), "mystery")

    def test_colour_for_looks_up_the_extension(self):
        style = Style(enabled=True)
        self.assertEqual(style.colour_for("main.py"), style.extension_colours[".py"])
        self.assertIsNone(style.colour_for("Makefile"))
