"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)
        with self.assertRaises(ValueError):

    def test_case_2(self):
        tree = build_sample(self.root)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_3(self):
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)
        self.assertIn('alpha.txt', text)

