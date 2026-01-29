import unittest

def sum_numbers(n1: int, n2: int) -> int:
    return n1 + n2

def divide_numbers(n1: int, n2: int) -> int:
    return n1 / n2

class SumTest(unittest.TestCase):
    
    def test_simple_sum(self):
        result = sum_numbers(5,5)
        self.assertEqual(result, 10)

    def test_negative_sum(self):
        result = sum_numbers(-10, -20)
        self.assertEqual(result, -30)

    def test_pos_negative_sum(self):
        result = sum_numbers(10, -8)
        self.assertEqual(result, 2)

    def test_raise_exception(self):
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(10, 0)