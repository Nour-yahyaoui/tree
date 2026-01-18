"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIsNone(entry)
        self.assertEqual(result, expected)
        self.assertEqual(stats.files, 2)

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(result, expected)

    def test_case_3(self):
        with self.assertRaises(ValueError):
        self.assertIn('alpha.txt', text)
        self.assertIsNone(entry)

