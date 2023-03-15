from unittest import TestCase
from problems.problem_2.solution.solution_problem_2 import validate_tree, TreeNode


class Problem2Tests(TestCase):
    def test_scenario_true(self):
        root = [2, 1, 3]
        root = self.convert_list_to_tree(root, 0)
        self.assertTrue(validate_tree(root))

    def test_scenario_false(self):
        root = [5, 1, 4, None, None, 3, 6]
        root = self.convert_list_to_tree(root, 0)
        self.assertFalse(validate_tree(root))
        self.fail('x')

    def test_scenario_all_one_value(self):
        root = [5, 5, 5, 5, 5]
        root = self.convert_list_to_tree(root, 0)
        self.assertFalse(validate_tree(root))

    def convert_list_to_tree(self, data, index):
        node = None
        if index <= len(data):
            try:
                if data[index] == None:
                    return None
            except IndexError:
                return None
            node = TreeNode(val=data[index])
            node.left = self.convert_list_to_tree(data, 2 * index + 1)
            node.right = self.convert_list_to_tree(data, 2 * index + 2)
        return node
