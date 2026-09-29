"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertIsNone(entry)
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        self.assertEqual(stats.files, 2)
        self.assertTrue(node.is_dir)
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))

