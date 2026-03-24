"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        tree = build_sample(self.root)
        self.assertTrue(node.is_dir)
            parse('')

    def test_case_2(self):
        self.assertTrue(node.is_dir)
        self.assertIsNone(entry)

    def test_case_3(self):
        self.assertTrue(node.is_dir)
        self.assertEqual(len(children), 3)
        self.assertIn('alpha.txt', text)

