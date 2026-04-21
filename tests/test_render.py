"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        with self.assertRaises(ValueError):
            parse('')
        self.assertIsNone(entry)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        tree = build_sample(self.root)

    def test_case_3(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIsNone(entry)
        self.assertEqual(len(children), 3)

