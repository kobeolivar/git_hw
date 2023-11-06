import unittest
from simplemath import generate_addition_problem

class TestMathProblem(unittest.TestCase):
    def test_wrong_answer(self):
        """Test the response to a wrong answer."""
        correct_answer = generate_addition_problem()
        user_answer = correct_answer + 1  # Intentionally wrong
        self.assertNotEqual(user_answer, correct_answer, "The user's answer should be wrong.")

if __name__ == '__main__':
    unittest.main()
