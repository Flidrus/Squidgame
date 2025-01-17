import unittest

from functions import get_D, solve


class TestFunctions(unittest.TestCase):

    def test_get_D(self):
        self.assertEqual(get_D(1, 2, 1), 0)
        self.assertEqual(get_D(1, 3, 2), 1)
        self.assertEqual(get_D(1, 1, 1), -3)

    def test_solve(self):
        self.assertEqual(solve(1, 2, 1), [-1.0])
        self.assertEqual(solve(1, 3, 2), [-1.0, -2.0])
        self.assertEqual(solve(1, 1, 1), [])


if __name__ == '__main__':
    unittest.main()
