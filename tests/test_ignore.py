"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIsNone(entry)
        tree = build_sample(self.root)

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIn('alpha.txt', text)

    def test_case_3(self):
        self.assertIn('alpha.txt', text)
        with self.assertRaises(ValueError):
        tree = build_sample(self.root)

