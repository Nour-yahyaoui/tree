"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertTrue(node.is_dir)
        self.assertEqual(stats.files, 2)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_2(self):
        self.assertIsNone(entry)
        self.assertTrue(node.is_dir)
        tree = build_sample(self.root)
        self.assertFalse(ignore.matches('keep.txt', False))

