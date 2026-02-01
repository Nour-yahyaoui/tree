"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertEqual(len(children), 3)
        self.assertTrue(node.is_dir)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(result, expected)

    def test_case_3(self):
        self.assertEqual(result, expected)
            parse('')
        with self.assertRaises(ValueError):

