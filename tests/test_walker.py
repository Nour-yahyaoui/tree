"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertIn('alpha.txt', text)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        tree = build_sample(self.root)
        with self.assertRaises(ValueError):

    def test_case_3(self):
        self.assertIsNone(entry)
        self.assertTrue(node.is_dir)
        self.assertFalse(ignore.matches('keep.txt', False))

