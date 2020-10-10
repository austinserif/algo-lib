import unittest
from algo_lib import search

unsorted_mock_array = [5, 2, 3, 10, -3]

sorted_mock_array = [0, 1, 3, 4, 5, 7, 8, 9]

class SearchTestCase(unittest.TestCase):
    def testLinear(self):
        self.assertEqual(search.linear(unsorted_mock_array, 5), 0)
        self.assertEqual(search.linear(unsorted_mock_array, -3), 4)
        self.assertEqual(search.linear(unsorted_mock_array, 0), -1)
        self.assertEqual(search.linear(unsorted_mock_array, 10), 3)
        self.assertEqual(search.linear(unsorted_mock_array, 100), -1)
        
    def testBinary(self):
        self.assertEqual(search.binary(sorted_mock_array, 0, len(sorted_mock_array)-1, 5), 4)
        self.assertEqual(search.binary(sorted_mock_array, 0, len(sorted_mock_array)-1, 0), 0)
        self.assertEqual(search.binary(sorted_mock_array, 0, len(sorted_mock_array)-1, 9), 7)
        self.assertEqual(search.binary(sorted_mock_array, 0, len(sorted_mock_array)-1, 2), -1)
        self.assertEqual(search.binary(sorted_mock_array, 0, len(sorted_mock_array)-1, 14), -1)

if __name__ == '__main__':  
    unittest.main()