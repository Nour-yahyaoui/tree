"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(result, expected)
        self.assertEqual(len(children), 3)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_2(self):
            parse('')
        self.assertEqual(stats.files, 2)
        self.assertFalse(ignore.matches('keep.txt', False))
        tree = build_sample(self.root)

