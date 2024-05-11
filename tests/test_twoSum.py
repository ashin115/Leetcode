import unittest
from Programs.twoSum import twoSum


class TestTwoSum(unittest.TestCase):
    def test_two_sum_exists(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(twoSum(nums, target), expected)

    def test_two_sum_not_exists(self):
        nums = [1, 2, 3, 4]
        target = 10
        expected = []
        self.assertEqual(twoSum(nums, target), expected)

    def test_two_sum_with_duplicates(self):
        nums = [3, 2, 4, 2]
        target = 6
        expected = [1, 3]
        self.assertEqual(twoSum(nums, target), expected)

    def test_two_sum_with_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        expected = [0, 2]
        self.assertEqual(twoSum(nums, target), expected)

    def test_two_sum_with_single_element(self):
        nums = [5]
        target = 10
        expected = []
        self.assertEqual(twoSum(nums, target), expected)

    def test_two_sum_with_empty_list(self):
        nums = []
        target = 10
        expected = []
        self.assertEqual(twoSum(nums, target), expected)
