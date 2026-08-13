"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(len(children), 3)
        self.assertEqual(result, expected)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertIsNone(entry)
        self.assertEqual(result, expected)
        with self.assertRaises(ValueError):

