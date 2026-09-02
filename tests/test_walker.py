"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertEqual(stats.files, 2)
        self.assertEqual(len(children), 3)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        with self.assertRaises(ValueError):
            parse('')

    def test_case_3(self):
        self.assertEqual(stats.files, 2)
        self.assertEqual(result, expected)
            parse('')

