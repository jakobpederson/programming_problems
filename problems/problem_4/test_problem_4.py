from unittest import TestCase
from problems.utils.tree_node import TreeNode

from problems.problem_3.solution.solution_problem_3 import convert_list_to_tree_node
from problems.problem_4.solution.solution_problem_4 import zig_zag_level_order


class Problem4Tests(TestCase):
    def test_convert_list(self):
        data = [3, 9, 20, None, None, 15, 7]
        root = convert_list_to_tree_node(data, 0)
        result = zig_zag_level_order(root)
        expected = [[3], [20, 9], [15, 7]]
        self.assertEqual(expected, result)

    def test_convert_list_with_one_node(self):
        data = [1]
        root = convert_list_to_tree_node(data, 0)
        result = zig_zag_level_order(root)
        expected = [[1]]
        self.assertEqual(expected, result)

    def test_convert_list_with_no_nodes(self):
        data = []
        root = convert_list_to_tree_node(data, 0)
        result = zig_zag_level_order(root)
        expected = []
        self.assertEqual(expected, result)

    def test_convert_list_with_more_nodes(self):
        data = [3, 9, 20, None, None, 15, 7, None, None, 20, 21]
        root = convert_list_to_tree_node(data, 0)
        result = zig_zag_level_order(root)
        expected = [[3], [20, 9], [15, 7], [21, 20]]
        self.assertEqual(expected, result)
