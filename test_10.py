import unittest
from test_09 import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.FizzBuzz = FizzBuzz
     # test case for Fizz
     # happy flow
    def test_fizz(self):
        self.assertEqual('Fizz', FizzBuzz(3).fizzbuzz())

    def test_Buzz(self):
        self.assertEqual('Buzz', FizzBuzz(5).fizzbuzz())

    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz",FizzBuzz(10).fizzbuzz())


if __name__ == '__main__':
    unittest.main()
