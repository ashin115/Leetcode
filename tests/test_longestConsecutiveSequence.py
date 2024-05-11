import unittest
from Programs.Array.LongestConsecutiveSequence import longestConsecutiveSequence


class TestLongestConsecutiveSequence(unittest.TestCase):
    def test_empty_sequence(self):
        self.assertEqual(longestConsecutiveSequence([]), 0)

    def test_single_element_sequence(self):
        self.assertEqual(longestConsecutiveSequence([1]), 1)

    def test_consecutive_sequence(self):
        self.assertEqual(longestConsecutiveSequence([1, 2, 3, 4, 5]), 5)

    def test_non_consecutive_sequence(self):
        self.assertEqual(longestConsecutiveSequence([1, 3, 5, 7, 9]), 1)

    def test_duplicate_elements(self):
        self.assertEqual(longestConsecutiveSequence([1, 2, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(
            longestConsecutiveSequence([-5, -4, -3, -2, -1, 0, 1, 2, 3]), 9
        )

    def test_mixed_sequence(self):
        self.assertEqual(longestConsecutiveSequence([100, 4, 200, 1, 3, 2]), 4)
