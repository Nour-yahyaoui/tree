"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(stats.files, 2)
        self.assertEqual(len(children), 3)

    def test_case_2(self):
        self.assertIn('alpha.txt', text)
        self.assertEqual(len(children), 3)
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIsNone(entry)

