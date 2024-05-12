import unittest
from Leetcode.Array.palindrome import isPalindrome


class TestIsPalindrome(unittest.TestCase):
    def test_positive_number(self):
        self.assertTrue(isPalindrome(121))

    def test_negative_number(self):
        self.assertFalse(isPalindrome(-121))

    def test_non_palindrome(self):
        self.assertFalse(isPalindrome(123))

    def test_zero(self):
        self.assertTrue(isPalindrome(0))

    def test_single_digit(self):
        self.assertTrue(isPalindrome(5))

    def test_large_number(self):
        self.assertTrue(isPalindrome(1234321))

