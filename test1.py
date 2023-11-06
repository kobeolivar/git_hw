import unittest
from simplemath import generate_addition_problem, check_answer

class TestAdditionProblem(unittest.TestCase):
    def test_generate_addition_problem(self):
        """Test that the addition problem generates integers and sums correctly."""
        result = generate_addition_problem()
        self.assertIsInstance(result, int, "The result should be an integer.")
        self.assertTrue(2 <= result <= 200, "Sum should be between 2 and 200.")

    def test_check_answer_addition(self):
        """Test the checking of the correct answer for an addition problem."""
        self.assertIsNone(check_answer(5, 5), "The check_answer function should return None for a correct answer.")
        with self.assertRaises(ValueError):  # Checking for ValueError now
            check_answer(5, 3)

if __name__ == '__main__':
    unittest.main()
