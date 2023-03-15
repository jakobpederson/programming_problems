from unittest import TestCase
from problems.problem_1.solution.solution_problem_1 import get_square


class ProblemOneTests(TestCase):
    def test_x(self):
        coords = [(1, 2), (3, 4), (6, 5), (5, 3)]
        result = get_square(coords)
        expected = [(1, 5), (1, 2), (6, 2), (6, 5)]
        self.assertCountEqual(expected, result)
