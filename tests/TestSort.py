import unittest
from algo_lib import sort

unsorted_mock_array = [5, 2, 3, 10, -3]
sorted_mock_array_decreasing = [10, 5, 3, 2, -3]
sorted_mock_array_increasing = [-3, 2, 3, 5, 10]

class SortTestCase(unittest.TestCase):
    def testMerge(self):
        sort.merge(unsorted_mock_array) # sort mock array increasing
        self.assertEqual(sorted_mock_array_increasing, unsorted_mock_array)

        sort.merge(unsorted_mock_array, False) #sort mock array decreasing
        self.assertEqual(sorted_mock_array_decreasing, unsorted_mock_array)

if __name__ == '__main__':  
    unittest.main()