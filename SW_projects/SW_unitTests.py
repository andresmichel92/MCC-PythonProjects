import unittest
import filecmp
import os
import time
from datetime import timedelta


class Test_fcm_method(unittest.TestCase):

    # Test if two different files are equal
    def test_one(self):
        self.assertFalse(filecmp.cmp("file1.txt", "file2.txt"))

    # Test if two different files are equal
    def test_two(self):
        self.assertFalse(filecmp.cmp("file1.txt", "file3.txt"))


class test_time_method(unittest.TestCase):
    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

    def test_fast(self):
        self.assertEqual(1, 1)

    def test_slow(self):
        time.sleep(0.5)
        self.assertEqual(1, 1)


class test_time2_method(unittest.TestCase):
    def test_t_one(self):
        local_time_month = time.localtime().tm_mon
        print(local_time_month)
        self.assertEqual(local_time_month, 2)


if __name__ == '__main__':
    unittest.main()
