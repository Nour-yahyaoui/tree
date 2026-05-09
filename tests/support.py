"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
            parse('')
        with self.assertRaises(ValueError):
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIn('alpha.txt', text)

    def test_case_3(self):
        self.assertEqual(len(children), 3)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(result, expected)

