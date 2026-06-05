"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        with self.assertRaises(ValueError):
        self.assertEqual(len(children), 3)
        self.assertIsNone(entry)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertTrue(node.is_dir)

    def test_case_3(self):
        self.assertEqual(len(children), 3)
        self.assertIn('alpha.txt', text)
        self.assertEqual(result, expected)

