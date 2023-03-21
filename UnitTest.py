import unittest
from A import A


class TestA(unittest.TestCase):
    def test_get_info(self):
        a = A(123)
        expected_output = 123
        self.assertEqual(a.get_int(), expected_output)

    def test_repr(self):
        a = A(123)
        expected_output = "A: 123"
        self.assertEqual(repr(a), expected_output)

    def test_add(self):
        a = A(123)
        b = A(456)
        expected_output = 579
        self.assertEqual(a + b, expected_output)


if __name__ == '__main__':
    unittest.main()
