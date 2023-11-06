import unittest
from simplemath import generate_addition_problem

class TestMathProblem(unittest.TestCase):
    def test_generate_addition_problem(self):
        """Test that the addition problem generates integers and sums correctly."""
        sum = generate_addition_problem()
        self.assertIsInstance(sum, int, "The result should be an integer.")
        self.assertTrue(2 <= sum <= 200, "Sum should be between 2 and 200.")

if __name__ == '__main__':
    unittest.main()
