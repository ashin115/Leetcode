import unittest
from Leetcode.Array.twoSum import twoSum


class TestTwoSum(unittest.TestCase):
    def test_two_sum_exists(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(twoSum(nums, target), expected)


    def test_two_sum_with_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        expected = [0, 2]
        self.assertEqual(twoSum(nums, target), expected)

