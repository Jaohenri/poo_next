"""
Unit tests module for basic arithmetic operations.

This module contains unit tests for arithmetic functions including
sum and divide operations, testing various scenarios including edge cases.
"""

import unittest


def sum_numbers(n1: int, n2: int) -> int:
    """
    Adds two numbers and returns their sum.
    
    Args:
        n1 (int): The first number.
        n2 (int): The second number.
    
    Returns:
        int: The sum of n1 and n2.
    """
    return n1 + n2


def divide_numbers(n1: int, n2: int) -> int:
    """
    Divides two numbers and returns the result.
    
    Args:
        n1 (int): The dividend.
        n2 (int): The divisor.
    
    Returns:
        int: The result of the division.
    
    Raises:
        ZeroDivisionError: If n2 is zero.
    """
    return n1 / n2

class SumTest(unittest.TestCase):
    """
    Test suite for arithmetic operations.
    
    Tests various scenarios for addition and division operations,
    including normal cases, edge cases, and exception handling.
    """

    def test_simple_sum(self):
        """Test addition of two positive numbers."""
        result = sum_numbers(5, 5)
        self.assertEqual(result, 10)

    def test_negative_sum(self):
        """Test addition of two negative numbers."""
        result = sum_numbers(-10, -20)
        self.assertEqual(result, -30)

    def test_pos_negative_sum(self):
        """Test addition of a positive and a negative number."""
        result = sum_numbers(10, -8)
        self.assertEqual(result, 2)

    def test_raise_exception(self):
        """Test that ZeroDivisionError is raised when dividing by zero."""
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(10, 0)
