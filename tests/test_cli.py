"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        with self.assertRaises(ValueError):
        self.assertEqual(len(children), 3)
        self.assertTrue(node.is_dir)
        tree = build_sample(self.root)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        tree = build_sample(self.root)

    def test_case_3(self):
        tree = build_sample(self.root)
        with self.assertRaises(ValueError):
            parse('')

