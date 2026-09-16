"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        tree = build_sample(self.root)
        with self.assertRaises(ValueError):
            parse('')

    def test_case_2(self):
        self.assertIsNone(entry)
        self.assertEqual(stats.files, 2)

    def test_case_3(self):
        self.assertEqual(result, expected)
        self.assertIn('alpha.txt', text)
        tree = build_sample(self.root)

