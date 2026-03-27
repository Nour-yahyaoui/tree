"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        self.assertIn('alpha.txt', text)
        self.assertIsNone(entry)
        self.assertEqual(result, expected)

    def test_case_2(self):
        with self.assertRaises(ValueError):
        self.assertEqual(stats.files, 2)

    def test_case_3(self):
            parse('')
        self.assertIsNone(entry)
        tree = build_sample(self.root)

