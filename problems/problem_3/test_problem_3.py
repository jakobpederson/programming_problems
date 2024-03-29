from unittest import TestCase, skipIf
from datetime import datetime

from problems.utils.tree_node import TreeNode
from problems.problem_3.solution.solution_problem_3 import convert_list_to_tree_node


@skipIf(
    datetime.now().date != datetime(2023, 7, 1),
    'LeetCode converts lists to linkedlists in a different way and I\'ll need to figure out how they do that',
)
class Problem3Tests(TestCase):
    def test_convert_list(self):
        data = [2, 1, 3]
        root = convert_list_to_tree_node(data, 0)
        expected = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
        self.assertEqual(expected.val, root.val)
        self.assertEqual(expected.left.val, root.left.val)
        self.assertEqual(expected.right.val, root.right.val)

    def test_convert_longer_list(self):
        #            1
        #         2     3
        #        4 5   6  7
        #       8
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        root = convert_list_to_tree_node(data, 0)
        self.assertEqual(1, root.val)
        self.assertEqual(2, root.left.val)
        self.assertEqual(3, root.right.val)
        self.assertEqual(4, root.left.left.val)
        self.assertEqual(5, root.left.right.val)
        self.assertEqual(6, root.right.left.val)
        self.assertEqual(7, root.right.right.val)
        self.assertEqual(8, root.left.left.left.val)

    def test_convert(self):
        #            3
        #         9     20
        #            15     7
        #                20  21
        data = [3, 9, 20, None, None, 15, 7, 20, 21]
        root = convert_list_to_tree_node(data, 0)
        self.assertEqual(3, root.val)
        self.assertEqual(9, root.left.val)
        self.assertEqual(20, root.right.val)
        self.assertEqual(None, root.left.left)
        self.assertEqual(None, root.left.right)
        self.assertEqual(15, root.right.left.val)
        self.assertEqual(20, root.right.left.left.val)
        self.assertEqual(21, root.right.left.right.val)
        self.assertEqual(7, root.right.right.val)
        self.assertEqual(None, root.right.right.left)
        self.assertEqual(None, root.right.right.right)
