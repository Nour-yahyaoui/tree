"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(len(children), 3)
        tree = build_sample(self.root)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        tree = build_sample(self.root)
        self.assertTrue(node.is_dir)
        self.assertEqual(len(children), 3)
        self.assertIsNone(entry)

