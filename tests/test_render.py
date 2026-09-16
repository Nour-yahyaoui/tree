"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        self.assertTrue(node.is_dir)
        self.assertEqual(len(children), 3)
        tree = build_sample(self.root)

    def test_case_2(self):
        self.assertTrue(node.is_dir)
        self.assertEqual(stats.files, 2)

    def test_case_3(self):
        self.assertTrue(node.is_dir)
        with self.assertRaises(ValueError):
            parse('')

