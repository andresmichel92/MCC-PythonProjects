import Sorting_Algorithm_1 as S1
import unittest
from unittest import mock
import time as t
import os

class TestSortingAlgorithm1(unittest.TestCase):

    def test_generate_data(self):
        list_1 = [1, 2, 3]
        time_stamp = t.time()
        S1.generate_data(list_1, time_stamp)
        assert len(S1.data) != 0

    def test_generate_end_data(self):
        time_stamp = t.time()
        S1.generate_end_data(time_stamp)
        assert S1.data[6] == 'Duration: '

    def test_set_input_data(self):
        at = S1.set_input_data("test3.csv")
        assert at == [1, 2, 3]

    def test_set_output_data(self):
        if os.path.exists('unittest_output.csv'):
            os.remove('unittest_output.csv')
        S1.set_output_data("unittest_output.csv", [1, 2, 3])
        os.path.isfile('unittest_output.csv')

    def test_execute_merge_sort(self):
        lista2 = [99.5, 100, 61, 3.33, 1, 0.3, 22]
        merge_sorted = S1.execute_merge_sort(lista2)
        assert merge_sorted[0] == 0.3

    def test_execute_quick_sort(self):
        lista2 = [99.5, 100, 61, 3.33, 1, 0.3, 22]
        quick_sorted = S1.execute_quick_sort(lista2)
        assert quick_sorted[0] == 0.3

    def test_execute_heap_sort(self):
        lista2 = [99.5, 100, 61, 3.33, 1, 0.3, 22]
        heap_sorted = S1.execute_heap_sort(lista2)
        assert heap_sorted[0] == 0.3

if __name__ == '__main__':
    unittest.main()
