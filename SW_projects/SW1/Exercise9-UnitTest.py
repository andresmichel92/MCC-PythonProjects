from SW_projects.SW1 import Exercise9 as E9
import unittest
from unittest import mock


class TestExercise9(unittest.TestCase):

    def test_ask_number(self):
        with mock.patch('builtins.input', return_value='1'):
            assert E9.ask_number() == int(1)




if __name__ == '__main__':
    unittest.main()

