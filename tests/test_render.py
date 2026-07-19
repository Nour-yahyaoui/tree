"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertTrue(node.is_dir)
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)
        tree = build_sample(self.root)

    def test_case_2(self):
        with self.assertRaises(ValueError):
        self.assertIn('alpha.txt', text)

    def test_case_3(self):
        self.assertTrue(node.is_dir)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIn('alpha.txt', text)

