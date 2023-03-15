class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self, *args, **kwargs):
        return f"TreeNode val {self.val} left {self.left.val if self.left else None}, right {self.right.val if self.right else None}"


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
