"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertEqual(len(children), 3)
        self.assertEqual(result, expected)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        self.assertEqual(stats.files, 2)
        with self.assertRaises(ValueError):

    def test_case_3(self):
        self.assertEqual(len(children), 3)
        self.assertTrue(node.is_dir)
        self.assertIsNone(entry)

