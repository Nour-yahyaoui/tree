"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        with self.assertRaises(ValueError):
            parse('')
        self.assertEqual(stats.files, 2)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
            parse('')

    def test_case_3(self):
        self.assertEqual(stats.files, 2)
        self.assertTrue(node.is_dir)
        self.assertEqual(result, expected)

