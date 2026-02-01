"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertIn('alpha.txt', text)
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        with self.assertRaises(ValueError):
        self.assertTrue(node.is_dir)
        self.assertEqual(len(children), 3)
        self.assertEqual(result, expected)

