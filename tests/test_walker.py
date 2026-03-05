"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(stats.files, 2)
        tree = build_sample(self.root)
        self.assertEqual(result, expected)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)
        tree = build_sample(self.root)

