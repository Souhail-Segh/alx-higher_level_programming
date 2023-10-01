#!/usr/bin/python3
''' Test Cases for max integer '''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestIntegerMethods(unittest.TestCase):

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 3, 5]), 5)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 6, 5]), 6)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_integer_float_elements(self):
        self.assertAlmostEqual(max_integer([1, 3, 5.2]), 5.2)

    def test_no_args(self):
        self.assertIsNone(max_integer())

    def test_not_list_type(self):
        with self.assertRaises(TypeError):
            max_integer(True)

    def test_not_list_integer(self):
        with self.assertRaises(TypeError):
            max_integer(1)

        with self.assertRaises(TypeError):
            max_integer([1, '2', False])

    def test_max_first_element(self):
        self.assertEqual(max_integer([5, 1, 3]), 5)

    def test_one_negatif(self):
        self.assertEqual(max_integer([4, -1, 0]), 4)

    def test_all_negatives(self):
        self.assertEqual(max_integer([-3, -5, -7]), -3)
