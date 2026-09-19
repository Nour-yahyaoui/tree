"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        self.assertIsNone(entry)
        self.assertIn('alpha.txt', text)
        self.assertTrue(node.is_dir)

    def test_case_2(self):
            parse('')
        self.assertIn('alpha.txt', text)

    def test_case_3(self):
        with self.assertRaises(ValueError):
        tree = build_sample(self.root)
        self.assertTrue(node.is_dir)

