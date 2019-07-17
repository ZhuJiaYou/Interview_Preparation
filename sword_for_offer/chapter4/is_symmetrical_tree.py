import sys
sys.path.append("..")
from utils import deserialize_tree, TreeNode


def is_symmetrical_bitree(root):
    nodes_lr = []
    nodes_rl = []

    def trverse_lr(root):
        nonlocal nodes_lr
        if not root:
            nodes_lr.append("$")
            return
        nodes_lr.append(root.val)
        trverse_lr(root.left)
        trverse_lr(root.right)

    def trverse_rl(root):
        nonlocal nodes_rl
        if not root:
            nodes_rl.append("$")
            return
        nodes_rl.append(root.val)
        trverse_rl(root.right)
        trverse_rl(root.left)
    
    trverse_lr(root)
    trverse_rl(root)
    return nodes_lr == nodes_rl


def is_symmetrical_bitree2(root):
    stack = root and [(root.left, root.right)]
    while stack:
        p1, p2 = stack.pop()
        if not p1 and not p2:
            continue
        if not p1 or not p2:
            return False
        if p1.val != p2.val:
            return False
        stack.append((p1.left, p2.right))
        stack.append((p1.right, p2.left))
    return True


if __name__ == "__main__":
    t1 = '8,6,5,$,$,7,$,$,6,7,$,$,5,$,$'
    t2 = '8,6,5,$,$,7,$,$,9,7,$,$,5,$,$'
    t3 = '7,7,7,$,$,7,$,$,7,7,$,$,$'
    t1 = deserialize_tree(t1)
    t2 = deserialize_tree(t2)
    t3 = deserialize_tree(t3)
    print(is_symmetrical_bitree2(t1))
    print(is_symmetrical_bitree2(t2))
    print(is_symmetrical_bitree2(t3))
