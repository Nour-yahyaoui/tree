"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        with self.assertRaises(ValueError):
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        tree = build_sample(self.root)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_3(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(result, expected)
        tree = build_sample(self.root)

