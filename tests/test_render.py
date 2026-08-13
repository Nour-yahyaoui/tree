"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(stats.files, 2)
        with self.assertRaises(ValueError):
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        self.assertTrue(node.is_dir)
        with self.assertRaises(ValueError):

    def test_case_3(self):
        with self.assertRaises(ValueError):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIn('alpha.txt', text)

