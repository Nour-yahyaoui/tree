"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIn('alpha.txt', text)
        with self.assertRaises(ValueError):
        self.assertIsNone(entry)

    def test_case_2(self):
        self.assertEqual(len(children), 3)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIn('alpha.txt', text)
        self.assertEqual(stats.files, 2)

