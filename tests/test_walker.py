"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        tree = build_sample(self.root)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        self.assertEqual(result, expected)
        self.assertEqual(stats.files, 2)
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))

