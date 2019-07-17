import sys
sys.path.append("..")
from utils import deserialize_tree, TreeNode, is_same_tree


def mirror_tree(root):
    if root:
        mirror_tree(root.left)
        mirror_tree(root.right)
        root.left, root.right = root.right, root.left
    return root


def mirror_tree2(root):
    stack = []
    stack.append(root)
    stack.append(root)
    while stack:
        p = stack.pop()
        if p and stack and p == stack[-1]:
            stack.append(p.right)
            stack.append(p.right)
            stack.append(p.left)
            stack.append(p.left)
        elif p:
            p.right, p.left = p.left, p.right
    return root


def mirror_tree3(root):
    stack = root and [root]
    while stack:
        p = stack.pop()
        if p:
            p.left, p.right = p.right, p.left
            stack += p.right, p.left
    return root


if __name__ == '__main__':
    t1 = '8,6,5,$,$,7,$,$,10,9,$,$,11,$,$'
    t2 = '8,10,11,$,$,9,$,$,6,7,$,$,5,$,$'
    t1 = deserialize_tree(t1)
    t2 = deserialize_tree(t2)
    print(is_same_tree(t2, mirror_tree3(t1)))
