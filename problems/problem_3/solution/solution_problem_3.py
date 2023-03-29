from problems.utils.tree_node import TreeNode


def convert_list_to_tree_node(data, index):
    # TODO when hitting a None adjust so that the next node gets the corresponding
    # values that should have gone to the node where the None is
    node = None
    if index <= len(data):
        try:
            if data[index] == None:
                return None
        except IndexError:
            return None
        if data[index - 1] == None:
            data = data[index - 1 :]
            index = 0
        node = TreeNode(val=data[index])
        node.left = convert_list_to_tree_node(data, 2 * index + 1)
        node.right = convert_list_to_tree_node(data, 2 * index + 2)
    return node
