"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)
        with self.assertRaises(ValueError):

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        self.assertIsNone(entry)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(result, expected)

