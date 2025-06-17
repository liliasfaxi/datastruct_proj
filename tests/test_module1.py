# tests/test_module1.py

import unittest
from my_proj.module1 import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
    
    def test_mult(self):
        self.assertEqual(self.calc.mult(1,0),0)
        self.assertEqual(self.calc.mult(10,-1),-10)
        
   
if __name__ == '__main__':
    unittest.main()
