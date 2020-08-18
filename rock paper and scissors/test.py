import rps
import unittest
class Tester(unittest.TestCase):

    def test_condition1(self):
        obj=rps.Rps()
        self.assertEqual(obj.game( ),"incorrect input")
if __name__ == "__main__":
    unittest.main()  