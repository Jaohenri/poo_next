import unittest

def sum(n1: int, n2: int) -> int:
    return n1 + n2

class SumTest(unittest.TestCase):
    
    def test_simple_sum(self):
        result = sum(5,5)
        self.assertEqual(result, 10)