"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIn('alpha.txt', text)
        self.assertTrue(node.is_dir)
        self.assertEqual(len(children), 3)
        tree = build_sample(self.root)

    def test_case_2(self):
        self.assertEqual(result, expected)
        self.assertTrue(node.is_dir)

    def test_case_3(self):
        self.assertEqual(stats.files, 2)
        self.assertEqual(result, expected)
        tree = build_sample(self.root)

