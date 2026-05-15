"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertEqual(len(children), 3)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
            parse('')
        self.assertIsNone(entry)
        self.assertTrue(node.is_dir)
        with self.assertRaises(ValueError):

