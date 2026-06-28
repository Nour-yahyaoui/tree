"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertEqual(stats.files, 2)
            parse('')
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_2(self):
        self.assertEqual(stats.files, 2)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_3(self):
        with self.assertRaises(ValueError):
        self.assertEqual(stats.files, 2)
        self.assertEqual(result, expected)

