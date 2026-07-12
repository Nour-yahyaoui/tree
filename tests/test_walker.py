"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
            parse('')
        self.assertFalse(ignore.matches('keep.txt', False))

