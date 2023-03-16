from unittest import TestCase
from problems.utils.tree_node import TreeNode
from problems.problem_3.solution.solution_problem_3 import convert_list_to_tree_node


class Problem3Tests(TestCase):
    def test_convert_list(self):
        data = [2, 1, 3]
        root = convert_list_to_tree_node(data, 0)
        expected = TreeNode(val=2, left=1, right=3)
        self.assertEqual(expected.val, root.val)
        self.assertEqual(expected.left, root.left)
        self.assertEqual(expected.left, root.left)
