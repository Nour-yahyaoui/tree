"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertTrue(node.is_dir)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        self.assertIsNone(entry)
        self.assertEqual(result, expected)

    def test_case_3(self):
        self.assertEqual(stats.files, 2)
        self.assertEqual(len(children), 3)
        self.assertEqual(result, expected)

