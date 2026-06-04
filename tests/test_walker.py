"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(stats.files, 2)
            parse('')

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        tree = build_sample(self.root)
        with self.assertRaises(ValueError):
        self.assertIsNone(entry)

