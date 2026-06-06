"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        self.assertFalse(ignore.matches('keep.txt', False))
        with self.assertRaises(ValueError):
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        self.assertTrue(node.is_dir)
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        self.assertEqual(len(children), 3)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertTrue(node.is_dir)

