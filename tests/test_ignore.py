"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertTrue(node.is_dir)
        tree = build_sample(self.root)
        self.assertEqual(stats.files, 2)
        self.assertEqual(len(children), 3)

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        tree = build_sample(self.root)

    def test_case_3(self):
        self.assertEqual(result, expected)
        self.assertTrue(node.is_dir)
        with self.assertRaises(ValueError):

