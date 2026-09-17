"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertEqual(result, expected)
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_2(self):
        self.assertEqual(stats.files, 2)
        self.assertEqual(result, expected)

    def test_case_3(self):
        tree = build_sample(self.root)
        self.assertEqual(result, expected)
        self.assertIn('alpha.txt', text)

