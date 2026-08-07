"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertIsNone(entry)
        self.assertEqual(len(children), 3)
        self.assertEqual(stats.files, 2)

    def test_case_2(self):
        self.assertEqual(len(children), 3)
        self.assertIn('alpha.txt', text)

    def test_case_3(self):
            parse('')
        self.assertTrue(node.is_dir)
        tree = build_sample(self.root)

