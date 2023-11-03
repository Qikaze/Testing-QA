import whitebox_test
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(whitebox_test.add(2, 3), 5)
        self.assertEqual(whitebox_test.add(0, 0), 0)
        self.assertEqual(whitebox_test.add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()