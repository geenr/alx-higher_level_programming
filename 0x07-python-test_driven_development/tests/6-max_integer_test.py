#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_maximum_numb(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3, 4, 5, 6, 7]), 7)
    def test_negative_num(self):
        self.assertEqual(max_integer([-2, -5]), -2)
    def test_float_num(self):
        self.assertEqual(max_integer([3.4, 1.2, 2.5]), 3.4)
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    def test_single_num(self):
        self.assertEqual(max_integer([2]), 2)
    def test_string(self):
        self.assertEqual(max_integer(["me", "is", "name"]), "name")

if __name__ == '__main__':
    unittest.main()
