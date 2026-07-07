"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(len(children), 3)
        self.assertIn('alpha.txt', text)
        self.assertEqual(stats.files, 2)
        self.assertIsNone(entry)

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIsNone(entry)

    def test_case_3(self):
        self.assertEqual(result, expected)
            parse('')
        self.assertEqual(len(children), 3)

