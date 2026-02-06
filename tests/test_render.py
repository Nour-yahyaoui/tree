"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        with self.assertRaises(ValueError):
        self.assertEqual(stats.files, 2)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(len(children), 3)

    def test_case_2(self):
        self.assertTrue(node.is_dir)
        self.assertIsNone(entry)

    def test_case_3(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(stats.files, 2)
        self.assertIsNone(entry)

