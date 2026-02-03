"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIn('alpha.txt', text)
        self.assertIsNone(entry)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_2(self):
        self.assertEqual(result, expected)
        with self.assertRaises(ValueError):
            parse('')
        self.assertTrue(node.is_dir)

