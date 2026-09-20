"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(len(children), 3)
            parse('')
        self.assertTrue(node.is_dir)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(stats.files, 2)

    def test_case_3(self):
        with self.assertRaises(ValueError):
            parse('')
        self.assertTrue(node.is_dir)

