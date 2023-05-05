from unittest import TestCase
from problems.utils.tree_node import TreeNode

from problems.problem_5.solution.solution_problem_5 import simplifyPath


class Problem5Tests(TestCase):
    def test_path(self):
        path = "/home/"
        result = simplifyPath(path)
        expected = "/home"
        self.assertEqual(expected, result)

    def test_path_with_dupe_slashes_and_double_periods(self):
        path = "/a/../../b/../c//.//"
        result = simplifyPath(path)
        expected = "/c"
        self.assertEqual(expected, result)

    def test_path_with_more_than_double_slashes_and_single_and_double_periods(self):
        path = "/a//b////c/d//././/.."
        result = simplifyPath(path)
        expected = "/a/b/c"
        self.assertEqual(expected, result)
