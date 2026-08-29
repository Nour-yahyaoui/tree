"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        with self.assertRaises(ValueError):
            parse('')

    def test_case_2(self):
        self.assertEqual(result, expected)
            parse('')
        self.assertEqual(stats.files, 2)
        with self.assertRaises(ValueError):

