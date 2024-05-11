import unittest
from Programs.romanToInteger import romanToInt


class TestRomanToInteger(unittest.TestCase):
    def test_valid_roman_numeral(self):
        self.assertEqual(romanToInt("III"), 3)
        self.assertEqual(romanToInt("IV"), 4)
        self.assertEqual(romanToInt("IX"), 9)
        self.assertEqual(romanToInt("LVIII"), 58)
        self.assertEqual(romanToInt("MCMXCIV"), 1994)

    def test_empty_string(self):
        self.assertEqual(romanToInt(""), 0)

    def test_invalid_roman_numeral(self):
        self.assertEqual(romanToInt("IIII"), 3)
        self.assertEqual(romanToInt("VV"), 10)
        self.assertEqual(romanToInt("IXI"), 9)

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(romanToInt("  VII  "), 7)

    def test_mixed_case(self):
        self.assertEqual(romanToInt("iV"), 4)
        self.assertEqual(romanToInt("Ix"), 9)
        self.assertEqual(romanToInt("mCmXcIv"), 1994)
