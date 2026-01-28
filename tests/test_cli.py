"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertEqual(result, expected)
        self.assertEqual(stats.files, 2)

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        tree = build_sample(self.root)
        self.assertEqual(len(children), 3)
        self.assertIsNone(entry)

