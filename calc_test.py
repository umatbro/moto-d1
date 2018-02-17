import unittest
from calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
