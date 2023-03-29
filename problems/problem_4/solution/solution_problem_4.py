from collections import defaultdict


def zig_zag_level_order(root):
    d = defaultdict(list)
    res = []

    def add(node, d, level):
        if node:
            d[level].append(node.val)
            add(node.left, d, level + 1)
            add(node.right, d, level + 1)
        return d

    add(root, d, 0)
    print(f"{d=}")
    for key, val in d.items():
        if key % 2 == 0:
            res.append(val)
        else:
            val.reverse()
            res.append(val)
    return res
