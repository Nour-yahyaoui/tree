"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(stats.files, 2)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_3(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(result, expected)
        self.assertIsNone(entry)

