import unittest
import calc 

class test_calc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(2 , 3), 5)

    def test_sub(self):
        self.assertEqual(calc.sub(2, 3), -1)

    def test_sub(self):
        self.assertEqual(calc.mul(2, 3), 6)
        

if __name__ == '__main__':
    unittest.main()
