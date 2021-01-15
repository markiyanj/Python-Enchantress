import unittest
import test_simple_calc as calc


class TestsSimpleCalc(unittest.TestCase):

    def test_add_func(self):
        self.assertEqual(calc.add(5, 3), 8)
        self.assertEqual(calc.add(-3, -2), -5)

    def test_subtract_func(self):
        self.assertEqual(calc.subtract(10, 4), 6)
        self.assertEqual(calc.subtract(-3, -7), 4)

    def test_multiply_func(self):
        self.assertEqual(calc.multiply(3, 2), 6)
        self.assertEqual(calc.multiply(-4, 2), -8)
        self.assertEqual(calc.multiply(0, 2), 0)

    def test_divide_func(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-4, 2), -2)
        self.assertRaises(ValueError, lambda: calc.divide(2, 0))


if __name__ == '__main__':
    unittest.main()
