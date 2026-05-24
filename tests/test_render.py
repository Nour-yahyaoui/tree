"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertEqual(stats.files, 2)
        self.assertFalse(ignore.matches('keep.txt', False))
        tree = build_sample(self.root)

    def test_case_2(self):
        self.assertEqual(stats.files, 2)
        self.assertTrue(node.is_dir)

    def test_case_3(self):
        tree = build_sample(self.root)
            parse('')
        with self.assertRaises(ValueError):

