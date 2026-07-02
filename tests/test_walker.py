"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        with self.assertRaises(ValueError):
            parse('')
        self.assertIn('alpha.txt', text)
        self.assertIsNone(entry)

    def test_case_2(self):
        self.assertEqual(len(children), 3)
        self.assertIsNone(entry)

    def test_case_3(self):
            parse('')
        self.assertIn('alpha.txt', text)
        self.assertTrue(node.is_dir)

