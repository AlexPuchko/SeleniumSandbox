import unittest
import calc

class CalcTest(unittest.TestCase):
 def test_add(self):
  self.assertEqual(calc.add(1, 2), 3)
 def test_sub(self):
  self.assertEqual(calc.sub(4, 2), 2)
 def test_mul(self):
  self.assertEqual(calc.mul(2, 5), 10)
 def test_div(self):
  self.assertEqual(calc.div(8, 4), 2)

if __name__ == '__main__':
    unittest.main()

# To run the tests you can execute from "Unittest" folder: 
# python -m unittest
# python -m unittest utest_calc.py - run tests from module utest_calc.py
# python -m unittest -v utest_calc.py - extended infirmation
# python -m unittest utest_calc.CalcTest - tests from class
# python -m unittest utest_calc.CalcTest.test_sub - run test test_sub


