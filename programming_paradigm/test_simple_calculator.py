import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Set up a calculator instance before each test"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition operation with various inputs"""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test mixed positive and negative
        self.assertEqual(self.calc.add(-5, 5), 0)
        # Test with zero
        self.assertEqual(self.calc.add(0, 0), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
    
    def test_subtraction(self):
        """Test subtraction operation with various inputs"""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test mixed positive and negative
        self.assertEqual(self.calc.subtract(5, -3), 8)
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
    
    def test_multiplication(self):
        """Test multiplication operation with various inputs"""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Test mixed positive and negative
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 1.5), 3.75)
    
    def test_division(self):
        """Test division operation with various inputs"""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test floating point result
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        # Test division by 1
        self.assertEqual(self.calc.divide(7, 1), 7)
        # Test division of negative numbers
        self.assertEqual(self.calc.divide(-9, -3), 3)
        # Test division resulting in zero
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test floating point division
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)

if __name__ == '__main__':
    unittest.main()