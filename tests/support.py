"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(len(children), 3)
        self.assertEqual(result, expected)
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        self.assertIsNone(entry)
        self.assertIn('alpha.txt', text)
        self.assertEqual(len(children), 3)
        with self.assertRaises(ValueError):

