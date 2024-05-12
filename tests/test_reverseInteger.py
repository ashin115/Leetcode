import unittest
from Leetcode.Math.reverseInteger import reverseInteger


class TestReverseInteger(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(reverseInteger(123), 321)

    def test_negative_number(self):
        self.assertEqual(reverseInteger(-456), -654)

    def test_zero(self):
        self.assertEqual(reverseInteger(0), 0)

    def test_max_int(self):
        self.assertEqual(reverseInteger(2147483647), 0)

    def test_min_int(self):
        self.assertEqual(reverseInteger(-2147483648), 0)

    def test_leading_zeros(self):
        self.assertEqual(reverseInteger(1200), 21)

    def test_single_digit(self):
        self.assertEqual(reverseInteger(5), 5)
