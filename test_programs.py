import unittest
from program1 import generate_numbers_divisible_by_5_and_7
from program2 import interleave_strings

class TestFunctions(unittest.TestCase):

    def test_generate_numbers_divisible_by_5_and_7(self):
        result = list(generate_numbers_divisible_by_5_and_7(100))
        self.assertEqual(result, [0, 35, 70])

    def test_interleave_strings(self):
        result = interleave_strings("AAAA", "1234567")
        self.assertEqual(result, "A1A2A3A4567")


if __name__ == "__main__":
    unittest.main()
