"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertTrue(node.is_dir)
        self.assertIn('alpha.txt', text)
        self.assertEqual(len(children), 3)

    def test_case_2(self):
        self.assertIsNone(entry)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_3(self):
        self.assertTrue(node.is_dir)
        self.assertFalse(ignore.matches('keep.txt', False))
        tree = build_sample(self.root)

