import unittest
from EX1 import safe_division

class TestModule(unittest.TestCase):
    def test_EX7(self):
        self.assertEqual(safe_division(4,4), 1)
        with self.assertRaises(ZeroDivisionError):
            safe_division(4,2)
            


if __name__=="__main__" :
    unittest.main()