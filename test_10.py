import unittest
from test_09 import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.FizzBuzz = FizzBuzz
     # test case for Fizz
     # happy flow
     # fizz case
    def test_fizz(self):
        self.assertEqual('Fizz', FizzBuzz(3).fizzbuzz())
     # Buzz case
    def test_Buzz(self):
        self.assertEqual('Buzz', FizzBuzz(5).fizzbuzz())
     # FizzBuzz Case
    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz",FizzBuzz(15).fizzbuzz())


if __name__ == '__main__':
    unittest.main()
