import unittest
from Programs.Array.searcha2DMatrix import searchMartix


class TestSearchMatrix(unittest.TestCase):
    def test_target_present(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        self.assertTrue(searchMartix(matrix, target))

    def test_target_not_present(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        self.assertFalse(searchMartix(matrix, target))

    def test_single_row_matrix(self):
        matrix = [[1, 3, 5, 7]]
        target = 3
        self.assertTrue(searchMartix(matrix, target))

    def test_single_column_matrix(self):
        matrix = [[1], [3], [5], [7]]
        target = 5
        self.assertTrue(searchMartix(matrix, target))

    def test_target_at_boundary(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 60
        self.assertTrue(searchMartix(matrix, target))
