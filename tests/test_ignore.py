"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        with self.assertRaises(ValueError):
        self.assertEqual(result, expected)

    def test_case_2(self):
        tree = build_sample(self.root)
        self.assertIsNone(entry)
        self.assertTrue(node.is_dir)
        self.assertFalse(ignore.matches('keep.txt', False))

