import unittest
from Programs.longestCommonPrefix import commonPrefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(commonPrefix([]), "")

    def test_single_string(self):
        self.assertEqual(commonPrefix(["hello"]), "hello")

    def test_common_prefix(self):
        self.assertEqual(commonPrefix(["flower", "flow", "flight"]), "fl")

    def test_no_common_prefix(self):
        self.assertEqual(commonPrefix(["dog", "cat", "mouse"]), "")

    def test_mixed_case(self):
        self.assertEqual(commonPrefix(["Hello", "Hello", "Hello"]), "Hello")
        self.assertEqual(commonPrefix(["Hello", "hello", "Hello"]), "")

    def test_empty_strings(self):
        self.assertEqual(commonPrefix(["", "", ""]), "")
        self.assertEqual(commonPrefix(["hello", "", "world"]), "")

    def test_single_character_strings(self):
        self.assertEqual(commonPrefix(["a", "a", "a"]), "a")
        self.assertEqual(commonPrefix(["a", "b", "c"]), "")
