import unittest
import utest_calc


calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(utest_calc.CalcTest))
print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
