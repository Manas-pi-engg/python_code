import unittest
import calc
import cal

class test_calc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(2 , 3), 5)

    def test_sub(self):
        self.assertEqual(calc.sub(2, 3), -1)

    def test_sub1(self):
        self.assertEqual(calc.mul(2, 3), 6)

    def test_add1(self):
            self.assertEqual(cal.add(2 , 3,4), 9)
    def test_add2(self):
            self.assertEqual(cal.sub(2 , 3,4), 1)
    def test_add3(self):
            self.assertEqual(cal.mul(2 , 3,4), 24)

if __name__ == '__main__':
    unittest.main()
