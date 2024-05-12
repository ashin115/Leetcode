import unittest
from Leetcode.Pointers.containerWithTheMostWater import maxArea


class TestMaxArea(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(maxArea([]), 0)

    def test_single_element(self):
        self.assertEqual(maxArea([1]), 0)

    def test_two_elements(self):
        self.assertEqual(maxArea([1, 2]), 1)

    def test_decreasing_heights(self):
        self.assertEqual(maxArea([5, 4, 3, 2, 1]), 6)

    def test_increasing_heights(self):
        self.assertEqual(maxArea([1, 2, 3, 4, 5]), 6)

    def test_all_same_heights(self):
        self.assertEqual(maxArea([3, 3, 3, 3, 3]), 12)

    def test_example_case(self):
        self.assertEqual(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
