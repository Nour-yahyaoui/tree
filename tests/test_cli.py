"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(len(children), 3)
        self.assertIsNone(entry)

    def test_case_2(self):
        self.assertEqual(len(children), 3)
        self.assertTrue(node.is_dir)

    def test_case_3(self):
        tree = build_sample(self.root)
        self.assertEqual(len(children), 3)
        self.assertFalse(ignore.matches('keep.txt', False))

