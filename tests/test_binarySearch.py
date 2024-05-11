import unittest
from Programs.BinarySearch.binarySearch import BinarySearch


class TestBinarySearch(unittest.TestCase):
    def test_target_present(self):
        nums = [1, 3, 5, 7, 9]
        target = 5
        self.assertEqual(BinarySearch(nums, target), 2)

    def test_target_not_present(self):
        nums = [1, 3, 5, 7, 9]
        target = 6
        self.assertEqual(BinarySearch(nums, target), -1)

    def test_empty_list(self):
        nums = []
        target = 5
        self.assertEqual(BinarySearch(nums, target), -1)

    def test_single_element_list(self):
        nums = [5]
        target = 5
        self.assertEqual(BinarySearch(nums, target), 0)

    def test_target_at_start(self):
        nums = [1, 3, 5, 7, 9]
        target = 1
        self.assertEqual(BinarySearch(nums, target), 0)

    def test_target_at_end(self):
        nums = [1, 3, 5, 7, 9]
        target = 9
        self.assertEqual(BinarySearch(nums, target), 4)

    def test_duplicate_elements(self):
        nums = [1, 3, 5, 5, 7]
        target = 5
        self.assertTrue(BinarySearch(nums, target) in [2, 3])
