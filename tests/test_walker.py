"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertTrue(node.is_dir)
            parse('')
        self.assertEqual(result, expected)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIn('alpha.txt', text)

    def test_case_3(self):
        self.assertEqual(result, expected)
        self.assertEqual(stats.files, 2)
        self.assertIn('alpha.txt', text)

