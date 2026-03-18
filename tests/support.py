"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(len(children), 3)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIsNone(entry)
        self.assertIn('alpha.txt', text)

    def test_case_2(self):
        self.assertIsNone(entry)
        self.assertEqual(stats.files, 2)

    def test_case_3(self):
        tree = build_sample(self.root)
        self.assertIsNone(entry)
        self.assertFalse(ignore.matches('keep.txt', False))

