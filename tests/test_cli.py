"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        with self.assertRaises(ValueError):
        self.assertIn('alpha.txt', text)
        self.assertEqual(len(children), 3)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        self.assertIsNone(entry)
        self.assertIn('alpha.txt', text)
        tree = build_sample(self.root)

