import unittest
from Programs.threesum import threeSum


class TestThreeSum(unittest.TestCase):
    def test_empty_list(self):
        nums = []
        expected = []
        self.assertEqual(threeSum(nums), expected)

    def test_no_triplets(self):
        nums = [1, 2, 3, 4, 5]
        expected = []
        self.assertEqual(threeSum(nums), expected)

    def test_one_triplet(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(sorted(threeSum(nums)), sorted(expected))

    def test_multiple_triplets(self):
        nums = [-2, 0, 1, 1, 2]
        expected = [[-2, 0, 2], [-2, 1, 1]]
        self.assertEqual(sorted(threeSum(nums)), sorted(expected))

    def test_duplicate_triplets(self):
        nums = [-1, 0, 1, 0]
        expected = [[-1, 0, 1]]
        self.assertEqual(threeSum(nums), expected)

    def test_large_input(self):
        nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
        expected = [
            [-4, -2, 6],
            [-4, 0, 4],
            [-4, 1, 3],
            [-4, 2, 2],
            [-2, -2, 4],
            [-2, 0, 2],
        ]
        self.assertEqual(sorted(threeSum(nums)), sorted(expected))
