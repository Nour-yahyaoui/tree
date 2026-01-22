"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertTrue(node.is_dir)
        self.assertEqual(stats.files, 2)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(len(children), 3)

    def test_case_2(self):
            parse('')
        self.assertEqual(result, expected)

    def test_case_3(self):
            parse('')
        self.assertEqual(result, expected)
        tree = build_sample(self.root)

