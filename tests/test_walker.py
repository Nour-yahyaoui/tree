"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertTrue(node.is_dir)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIsNone(entry)

    def test_case_2(self):
        self.assertIsNone(entry)
        self.assertTrue(node.is_dir)
        self.assertEqual(stats.files, 2)
        with self.assertRaises(ValueError):

