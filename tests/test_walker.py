"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        tree = build_sample(self.root)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIsNone(entry)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        self.assertIsNone(entry)
        self.assertEqual(len(children), 3)
        with self.assertRaises(ValueError):

