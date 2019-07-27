import copy
import sys
sys.path.append("..")
from utils import TreeNode, is_same_tree, preorder_traversal, inorder_traversal


def serialize_tree(root):
    if not root:
        return "$"
    return str(root.val) + "," + serialize_tree(root.left) + "," + serialize_tree(root.right)


def deserialize_tree(s):
    def deserialize(nodes):
        if len(nodes) < 1:
            return None
        if nodes[-1] == "$":
            nodes.pop()
            return None
        root = TreeNode(int(nodes.pop()))
        root.left = deserialize(nodes)
        root.right = deserialize(nodes)
        return root
    return deserialize(s.split(",")[::-1])


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left, t1.right = TreeNode(2), TreeNode(3)
    t1.left.left, t1.right.left, t1.right.right = TreeNode(4), TreeNode(5), TreeNode(6)
    t2 = copy.copy(t1)
    t3_str = serialize_tree(t1)
    print(t3_str)
    t3 = deserialize_tree(t3_str)
    print(is_same_tree(t1, t3))
    print(preorder_traversal(t3))
    print(inorder_traversal(t3))

