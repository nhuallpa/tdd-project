import unittest
from dollar import Dollar

class TestMoney(unittest.TestCase):
    def testMultiplation(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)

if __name__ == '__main__':
    unittest.main()