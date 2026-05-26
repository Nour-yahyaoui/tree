"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(len(children), 3)
        with self.assertRaises(ValueError):
        self.assertTrue(node.is_dir)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        with self.assertRaises(ValueError):
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        self.assertTrue(node.is_dir)
        self.assertIsNone(entry)
        self.assertFalse(ignore.matches('keep.txt', False))

