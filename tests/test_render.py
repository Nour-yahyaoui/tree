"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        self.assertTrue(node.is_dir)
        self.assertIsNone(entry)

    def test_case_2(self):
            parse('')
        self.assertFalse(ignore.matches('keep.txt', False))
        with self.assertRaises(ValueError):
        self.assertIn('alpha.txt', text)

