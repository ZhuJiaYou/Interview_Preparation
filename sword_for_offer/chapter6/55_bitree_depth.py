import sys
sys.path.append("..")
from utils import TreeNode, deserialize_tree


def bitree_depth(root):
    if not root:
            return 0
    if root.left and not root.right:
        return 1 + bitree_depth(root.left)
    elif root.right and not root.left:
        return 1 + bitree_depth(root.right)
    elif root.left and root.right:
        return 1 + max(bitree_depth(root.left), bitree_depth(root.right))
    else:
        return 1


if __name__ == '__main__':
    t1 = '1,2,4,$,$,5,7,$,$,$,3,$,6,$,$'
    t1 = deserialize_tree(t1)
    print(bitree_depth(t1))
