from problems.utils.tree_node import TreeNode


def convert_list_to_tree_node(data, index):
    node = None
    if index <= len(data):
        try:
            if data[index] == None:
                return None
        except IndexError:
            return None
        node = TreeNode(val=data[index])
        node.left = convert_list_to_tree_node(data, 2 * index + 1)
        node.right = convert_list_to_tree_node(data, 2 * index + 2)
    return node
