"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertTrue(node.is_dir)
        self.assertEqual(len(children), 3)

    def test_case_2(self):
        self.assertEqual(result, expected)
        self.assertIn('alpha.txt', text)

    def test_case_3(self):
        self.assertIn('alpha.txt', text)
        tree = build_sample(self.root)
        self.assertEqual(result, expected)

