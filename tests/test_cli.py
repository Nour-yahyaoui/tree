"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertIsNone(entry)
        self.assertEqual(stats.files, 2)
        with self.assertRaises(ValueError):

    def test_case_2(self):
        self.assertTrue(node.is_dir)
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        self.assertIsNone(entry)
        self.assertEqual(len(children), 3)
        with self.assertRaises(ValueError):

