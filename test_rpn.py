
import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_exp3(self):
        result = rpn.calculate("3 3 ^")
        self.assertEqual(27, result)
    def test_exp2(self):
        result = rpn.calculate("2 2 ^")
        self.assertEqual(4, result)
    def test_exp4(self):
        result = rpn.calculate("4 3 ^")
        self.assertEqual(64, result)
    def test_mult(self):
        result = rpn.calculate("4 3 *")
        self.assertEqual(12, result)
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_sub(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_div1(self):
        result = rpn.calculate("5 3 /")
        self.assertEqual(1, result)
    def test_div2(self):
        result = rpn.calculate("12 3 /")
        self.assertEqual(4, result)
    def test_badinput(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')
