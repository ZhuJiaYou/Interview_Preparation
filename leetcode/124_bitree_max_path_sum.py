from utils import TreeNode, deserialize_tree
import sys


def max_bitree_path_sum(root):
    max_sum = -sys.maxsize
    def max_end(node):
        if not node:
            return 0
        left = max_end(node.left)
        right = max_end(node.right)
        nonlocal max_sum
        max_sum = max(left+node.val+right, max_sum)
        return max(node.val+max(left, right), 0)
    max_end(root)
    return max_sum


if __name__ == '__main__':
    t = '-10,9,$,$,20,15,$,$,7,$,$'
    root = deserialize_tree(t)
    print(max_bitree_path_sum(root))
