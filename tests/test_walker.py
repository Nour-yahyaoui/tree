"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(stats.files, 2)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertIsNone(entry)

    def test_case_3(self):
        tree = build_sample(self.root)
        self.assertTrue(node.is_dir)
        self.assertEqual(stats.files, 2)

