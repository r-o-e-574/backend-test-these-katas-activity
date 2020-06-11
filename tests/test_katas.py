import unittest
import katas
from katas import *


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5,5), 10)

    def test_multiply(self):
        self.assertEqual(multiply(10,5), 50)

    def test_power(self):
        self.assertEqual(power(10, 3), 1000)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(10), 34)


if __name__ == '__main__':
    unittest.main()
