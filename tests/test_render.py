"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIsNone(entry)

    def test_case_2(self):
        tree = build_sample(self.root)
        self.assertIn('alpha.txt', text)
        self.assertIsNone(entry)
        self.assertTrue(node.is_dir)

