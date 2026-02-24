"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(len(children), 3)
        self.assertIsNone(entry)
        self.assertIn('alpha.txt', text)
        tree = build_sample(self.root)

    def test_case_2(self):
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        self.assertFalse(ignore.matches('keep.txt', False))
            parse('')
        tree = build_sample(self.root)

