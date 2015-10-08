import unittest
import os
from math import factorial
from compute_factorials import compute_from_files


class TestComputeFactorial(unittest.TestCase):

    def setUp(self):
        self.test_data = {}
        self.filenames = []
        for i in range(3):
            with open('test'+str(i), 'w') as f:
                f.write(str(i))
                self.test_data[i] = factorial(i)
                self.filenames.append('test'+str(i))

    def test_compute_from_files(self):
        """ Test compute_from_files function"""
        results = compute_from_files(self.filenames)
        for number, fact in results.items():
            with self.subTest(number=number):
                self.assertEqual(self.test_data[number], factorial(number))

    def tearDown(self):
        for f in self.filenames:
            os.remove(f)
