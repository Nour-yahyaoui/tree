"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertIn('alpha.txt', text)
            parse('')

    def test_case_2(self):
        tree = build_sample(self.root)
        self.assertIn('alpha.txt', text)
        self.assertEqual(stats.files, 2)
        self.assertEqual(len(children), 3)

