import unittest
from simplemath import generate_multiplication_problem, check_answer

class TestMultiplicationProblem(unittest.TestCase):
    def test_generate_multiplication_problem(self):
        """Test that the multiplication problem generates integers and products correctly."""
        result = generate_multiplication_problem()
        self.assertIsInstance(result, int, "The result should be an integer.")
        self.assertTrue(1 <= result <= 10000, "Product should be between 1 and 10000.")

    def test_check_answer_multiplication(self):
        """Test the checking of the correct answer for a multiplication problem."""
        self.assertIsNone(check_answer(20, 20), "The check_answer function should return None for a correct answer.")
        with self.assertRaises(ValueError):  # Checking for ValueError now
            check_answer(20, 30)


if __name__ == '__main__':
    unittest.main()
