"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertEqual(result, expected)
        tree = build_sample(self.root)

    def test_case_2(self):
        self.assertEqual(len(children), 3)
        self.assertTrue(node.is_dir)
        self.assertEqual(stats.files, 2)
        tree = build_sample(self.root)

