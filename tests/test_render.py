"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertEqual(len(children), 3)
        tree = build_sample(self.root)
        self.assertFalse(ignore.matches('keep.txt', False))

    def test_case_2(self):
        self.assertFalse(ignore.matches('keep.txt', False))
            parse('')
        self.assertEqual(stats.files, 2)
        self.assertEqual(result, expected)

