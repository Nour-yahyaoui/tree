"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        with self.assertRaises(ValueError):
        self.assertEqual(len(children), 3)
        self.assertEqual(result, expected)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(stats.files, 2)

    def test_case_3(self):
        tree = build_sample(self.root)
        self.assertEqual(stats.files, 2)
        self.assertEqual(len(children), 3)

