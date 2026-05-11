"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertTrue(node.is_dir)
        self.assertEqual(result, expected)
        self.assertEqual(stats.files, 2)

    def test_case_2(self):
        self.assertEqual(stats.files, 2)
        self.assertTrue(node.is_dir)
        self.assertIn('alpha.txt', text)
        tree = build_sample(self.root)

