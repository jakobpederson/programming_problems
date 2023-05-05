from unittest import TestCase

from problems.problem_6.solution.solution_problem_6 import find_second_largest


class Problem6Tests(TestCase):
    def test_find_second_largest(self):
        result = find_second_largest([3, 6, 1, 8, 4])
        self.assertEqual(result, 6)

    def test_find_second_largest_returns_none(self):
        result = find_second_largest([1, 1, 1])
        self.assertEqual(result, None)
