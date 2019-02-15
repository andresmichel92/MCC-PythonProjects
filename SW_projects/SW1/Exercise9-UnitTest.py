import Exercise9 as E9
import unittest
from unittest import mock


class TestExercise9(unittest.TestCase):

    def test_ask_number(self):
        with mock.patch('builtins.input', return_value='1'):
            assert E9.ask_number() == int(1)

    def test_small_romans(self):
        variable_t = 123
        assert type(E9.generate_romans(variable_t))== type("string")

    def test_large_romans(self):
        variable_t = 4500
        assert type(E9.generate_romans(variable_t))== type("string")

    def test_negative_romans(self):
        variable_t = -4500
        assert type(E9.generate_romans(variable_t)) == type("string")

    def test_million_romans(self):
        variable_t = 1000000
        assert E9.generate_romans(variable_t) == "_\nM"



if __name__ == '__main__':
    unittest.main()

