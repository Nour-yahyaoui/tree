"""Tests for the filesystem walker."""

from __future__ import annotations

import os
import stat
import unittest

from tests.support import TempTreeCase, names, relative_names
from treepy.node import Stats
from treepy.walker import WalkOptions, walk


class WalkerTests(TempTreeCase):
    def test_basic_tree_shape(self):
        self.sample()
        root = walk(self.root, WalkOptions(show_hidden=True), Stats())
        self.assertEqual(
            sorted(relative_names(root)),
            sorted(
                [
                    os.path.basename(self.root),
                    ".hidden",
                    ".hidden/secret.txt",
                    "alpha.txt",
                    "sub",
                    "sub/beta.py",
                    "sub/deep",
                    "sub/deep/gamma.md",
                ]
            ),
        )

    def test_entries_are_sorted_by_name(self):
        self.sample()
        root = walk(self.root, WalkOptions(show_hidden=True), Stats())
        self.assertEqual(
            [child.name for child in root.children], [".hidden", "alpha.txt", "sub"]
        )

    def test_hidden_entries_are_skipped_by_default(self):
        self.sample()
        root = walk(self.root, WalkOptions(), Stats())
        self.assertNotIn(".hidden", names(root))
        self.assertIn("alpha.txt", names(root))

    def test_stats_count_everything(self):
        self.sample()
        stats = Stats()
        walk(self.root, WalkOptions(show_hidden=True), stats)
        self.assertEqual(stats.dirs, 4)
        self.assertEqual(stats.files, 4)
        self.assertEqual(stats.errors, 0)

    def test_max_depth_limits_recursion(self):
        self.sample()
        root = walk(self.root, WalkOptions(max_depth=1), Stats())
        self.assertEqual([child.name for child in root.children], ["alpha.txt", "sub"])
        self.assertEqual(root.children[1].children, [])

    def test_max_depth_zero_lists_the_root_only(self):
        self.sample()
        root = walk(self.root, WalkOptions(max_depth=0), Stats())
        self.assertEqual(len(root.children), 0)

    def test_dirs_only_hides_files(self):
        self.sample()
        root = walk(self.root, WalkOptions(dirs_only=True), Stats())
        self.assertEqual([child.name for child in root.children], ["sub"])
        self.assertEqual([child.name for child in root.children[0].children], ["deep"])

    def test_sort_by_name_is_case_insensitive(self):
        self.make("Zeta.txt")
        self.make("alpha.txt")
        self.mkdir("Beta")
        root = walk(self.root, WalkOptions(), Stats())
        self.assertEqual(
            [child.name for child in root.children], ["alpha.txt", "Beta", "Zeta.txt"]
        )

    def test_reverse_sort(self):
        self.make("a.txt")
        self.make("b.txt")
        self.make("c.txt")
        root = walk(self.root, WalkOptions(reverse=True), Stats())
        self.assertEqual([child.name for child in root.children], ["c.txt", "b.txt", "a.txt"])

    def test_sort_by_size(self):
        self.make("small.txt", "x")
        self.make("big.txt", "x" * 100)
        root = walk(self.root, WalkOptions(sort_key="size"), Stats())
        self.assertEqual([child.name for child in root.children], ["small.txt", "big.txt"])

    def test_sort_none_keeps_directory_order(self):
        for name in ("one.txt", "two.txt", "three.txt"):
            self.make(name)
        root = walk(self.root, WalkOptions(sort_key="none"), Stats())
        self.assertEqual(len(root.children), 3)

    def test_unknown_sort_key_is_rejected(self):
        with self.assertRaises(ValueError):
            WalkOptions(sort_key="colour")

    def test_negative_depth_is_rejected(self):
        with self.assertRaises(ValueError):
            WalkOptions(max_depth=-1)

    def test_prune_empty_removes_childless_directories(self):
        self.mkdir("empty")
        self.make("full/file.txt")
        stats = Stats()
        root = walk(self.root, WalkOptions(prune_empty=True), stats)
        self.assertEqual([child.name for child in root.children], ["full"])
        self.assertEqual(stats.dirs, 2)

    def test_missing_root_reports_an_error(self):
        errors = []
        options = WalkOptions(error_hook=lambda path, error: errors.append(path))
        stats = Stats()
        root = walk(os.path.join(self.root, "nope"), options, stats)
        self.assertIsNotNone(root.error)
        self.assertEqual(stats.errors, 1)
        self.assertEqual(len(errors), 1)

    def test_quiet_hook_suppresses_stderr(self):
        stats = Stats()
        root = walk(os.path.join(self.root, "nope"), WalkOptions(error_hook=None), stats)
        self.assertEqual(stats.errors, 1)
        self.assertIsNotNone(root.error)

    def test_file_sizes_are_summed(self):
        self.make("a.txt", "12345")
        self.make("b.txt", "123")
        stats = Stats()
        walk(self.root, WalkOptions(), stats)
        self.assertEqual(stats.total_bytes, 8)
        self.assertEqual(stats.files, 2)

    def test_ignore_patterns_are_matched_on_relative_paths(self):
        self.make("keep.txt")
        self.make("skip.log")
        self.mkdir("logs")
        self.make("logs/old.log")
        from treepy.ignore import IgnoreSet

        ignore = IgnoreSet.from_patterns(["*.log"])
        root = walk(self.root, WalkOptions(ignore=ignore), Stats())
        self.assertEqual([child.name for child in root.children], ["keep.txt", "logs"])
        self.assertEqual(root.children[1].children, [])

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks are not supported here")
    def test_symlinks_are_reported_not_followed(self):
        self.make("real/file.txt")
        os.symlink(os.path.join(self.root, "real"), os.path.join(self.root, "link"))
        stats = Stats()
        root = walk(self.root, WalkOptions(), stats)
        link = root.find("link")
        self.assertIsNotNone(link)
        self.assertTrue(link.symlink)
        self.assertEqual(link.link_target, os.path.join(self.root, "real"))
        self.assertEqual(link.children, [])
        self.assertEqual(stats.symlinks, 1)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks are not supported here")
    def test_following_a_symlink_cycle_stops(self):
        self.mkdir("a")
        os.symlink(self.root, os.path.join(self.root, "a", "loop"))
        stats = Stats()
        root = walk(self.root, WalkOptions(follow_symlinks=True), stats)
        loop = root.find("a/loop")
        self.assertIsNotNone(loop)
        self.assertTrue(loop.cycle)
        self.assertEqual(loop.children, [])

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks are not supported here")
    def test_following_a_symlink_directory_lists_its_contents(self):
        self.make("real/file.txt")
        os.symlink(os.path.join(self.root, "real"), os.path.join(self.root, "link"))
        root = walk(self.root, WalkOptions(follow_symlinks=True), Stats())
        link = root.find("link")
        self.assertIsNotNone(link)
        self.assertEqual([child.name for child in link.children], ["file.txt"])

    @unittest.skipIf(not hasattr(os, "geteuid") or os.geteuid() == 0, "root ignores modes")
    def test_unreadable_directory_is_reported(self):
        self.mkdir("locked")
        os.chmod(os.path.join(self.root, "locked"), 0o000)
        self.addCleanup(os.chmod, os.path.join(self.root, "locked"), 0o755)
        stats = Stats()
        root = walk(self.root, WalkOptions(error_hook=lambda *_: None), stats)
        locked = root.find("locked")
        self.assertIsNotNone(locked.error)
        self.assertEqual(stats.errors, 1)

    def test_executable_bit_is_visible_in_stat_mode(self):
        path = self.make("run.sh", "#!/bin/sh\n")
        os.chmod(path, 0o755)
        mode = os.stat(path).st_mode
        self.assertTrue(mode & stat.S_IXUSR)
