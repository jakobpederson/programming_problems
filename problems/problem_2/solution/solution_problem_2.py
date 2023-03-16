def validate_tree(root):
    stack = []
    previous_val = float("-inf")
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        node = stack.pop()
        if node.val <= previous_val:
            return False
        previous_val = node.val
        current = node.right
    return True
