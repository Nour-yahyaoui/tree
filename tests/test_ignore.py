"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertEqual(stats.files, 2)
        with self.assertRaises(ValueError):

    def test_case_2(self):
        self.assertEqual(stats.files, 2)
            parse('')
        tree = build_sample(self.root)
        self.assertTrue(node.is_dir)

