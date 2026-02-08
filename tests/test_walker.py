"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertEqual(stats.files, 2)
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)

    def test_case_2(self):
        tree = build_sample(self.root)
        self.assertIsNone(entry)

    def test_case_3(self):
        with self.assertRaises(ValueError):
        self.assertIsNone(entry)
        self.assertEqual(len(children), 3)

