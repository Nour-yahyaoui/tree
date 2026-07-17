"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)
        with self.assertRaises(ValueError):
        self.assertEqual(stats.files, 2)

    def test_case_2(self):
        self.assertEqual(len(children), 3)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_3(self):
        self.assertEqual(result, expected)
        self.assertTrue(node.is_dir)
        self.assertIsNone(entry)

