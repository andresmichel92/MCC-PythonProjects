import unittest
import filecmp
import os


class Test_fcm_method(unittest.TestCase):

    # Test if two different files are equal
    def test_one(self):
        x = os.path.dirname(r'')
        self.assertFalse(filecmp.cmp("file1.txt", "file2.txt"))


class test_time_method(unittest.TestCase):

    # Test if time


if __name__ == '__main__':
    unittest.main()
