"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertEqual(stats.files, 2)
        self.assertEqual(len(children), 3)
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        self.assertTrue(node.is_dir)
            parse('')

    def test_case_3(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertTrue(node.is_dir)
        with self.assertRaises(ValueError):

