import unittest
import sys
import os

# This allows the test runner to find the 'src' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sorter import sort_list_ascending

class TestSorter(unittest.TestCase):
    """
    Test suite for the sort_list_ascending function.
    """

    def test_standard_case(self):
        """
        TC-01: Tests an unsorted list of positive integers.
        """
        self.assertEqual(sort_list_ascending([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])

    def test_empty_list(self):
        """
        TC-02: Tests an empty list.
        """
        self.assertEqual(sort_list_ascending([]), [])

    def test_duplicate_values(self):
        """
        TC-03: Tests a list containing duplicate values.
        """
        self.assertEqual(sort_list_ascending([4, 2, 5, 2, 4]), [2, 2, 4, 4, 5])

    def test_already_sorted(self):
        """
        TC-04: Tests a list that is already sorted.
        """
        self.assertEqual(sort_list_ascending([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_mixed_values(self):
        """
        TC-05: Tests a list with positive, negative, and zero values.
        """
        self.assertEqual(sort_list_ascending([-5, 10, 0, -1, 3]), [-5, -1, 0, 3, 10])

    def test_single_element(self):
        """
        TC-06: Tests a list with only one integer.
        """
        self.assertEqual(sort_list_ascending([42]), [42])

    def test_all_same_elements(self):
        """
        TC-07: Tests a list with all identical integers.
        """
        self.assertEqual(sort_list_ascending([7, 7, 7, 7]), [7, 7, 7, 7])

if __name__ == '__main__':
    unittest.main()