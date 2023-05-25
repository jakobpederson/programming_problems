from unittest import TestCase

from problems.problem_7.solution.solution_problem_7 import find_pairs


class Problem7Tests(TestCase):
    def test_find_pairs(self):
        result = find_pairs([2, 3, 5, 7, 8, 1])
        self.assertEqual(result, [(3, 7), (2, 8)])

    def test_find_pair_with_double_numbers(self):
        result = find_pairs([2, 3, 5, 7, 8, 1, 5])
        self.assertEqual(result, [(3, 7), (5, 5), (2, 8)])
