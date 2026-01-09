"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertIn('alpha.txt', text)
        self.assertEqual(len(children), 3)

    def test_case_2(self):
        self.assertEqual(len(children), 3)
        self.assertEqual(result, expected)
        self.assertFalse(ignore.matches('keep.txt', False))
        tree = build_sample(self.root)

