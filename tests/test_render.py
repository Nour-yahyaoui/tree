"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        with self.assertRaises(ValueError):
        self.assertTrue(node.is_dir)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_2(self):
        self.assertIsNone(entry)
        self.assertEqual(stats.files, 2)
        tree = build_sample(self.root)
        self.assertTrue(node.is_dir)

