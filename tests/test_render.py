"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertEqual(result, expected)
        self.assertTrue(node.is_dir)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        tree = build_sample(self.root)
        with self.assertRaises(ValueError):

    def test_case_3(self):
            parse('')
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)

