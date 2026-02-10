"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        with self.assertRaises(ValueError):
        self.assertTrue(node.is_dir)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(result, expected)

    def test_case_2(self):
        with self.assertRaises(ValueError):
        self.assertIn('alpha.txt', text)

    def test_case_3(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(len(children), 3)
        self.assertEqual(stats.files, 2)

