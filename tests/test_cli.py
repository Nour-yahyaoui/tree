"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        with self.assertRaises(ValueError):
        self.assertEqual(stats.files, 2)
        self.assertEqual(result, expected)

    def test_case_2(self):
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))

