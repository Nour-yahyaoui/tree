"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertEqual(result, expected)
        self.assertIsNone(entry)
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        self.assertIn('alpha.txt', text)
        self.assertIsNone(entry)
        with self.assertRaises(ValueError):

