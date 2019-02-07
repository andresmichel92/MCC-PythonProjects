import unittest
import filecmp
import os
import time


class Test_fcm_method(unittest.TestCase):

    # Test if two different files are equal
    def test_one(self):
        x = os.path.dirname(r'')
        self.assertFalse(filecmp.cmp("file1.txt", "file2.txt"))


class test_time_method(unittest.TestCase):

    # Test if time
    def test_t_one(self):
        gm_time = time.gmtime()
        local_time = time.localtime()
        self.assertTrue(int(gm_time)-(6*60*24) == int(time.localtime()))




if __name__ == '__main__':
    unittest.main()
