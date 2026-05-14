"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertEqual(len(children), 3)
        with self.assertRaises(ValueError):

    def test_case_2(self):
        self.assertEqual(len(children), 3)
        self.assertTrue(node.is_dir)
        with self.assertRaises(ValueError):
        self.assertFalse(ignore.matches('keep.txt', False))

