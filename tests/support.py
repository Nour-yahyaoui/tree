"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(stats.files, 2)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        tree = build_sample(self.root)
        with self.assertRaises(ValueError):
        self.assertFalse(ignore.matches('keep.txt', False))

