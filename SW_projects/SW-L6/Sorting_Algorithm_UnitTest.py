import Sorting_Algorithm_1 as S1
import unittest
from unittest import mock
import time as t


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




if __name__ == '__main__':
    unittest.main()
