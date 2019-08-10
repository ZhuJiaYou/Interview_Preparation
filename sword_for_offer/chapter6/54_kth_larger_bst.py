import sys
sys.path.append("..")
from utils import TreeNode, deserialize_tree


def find_kth_largest(root, k):
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            if k > 1:
                k -= 1
            else:
                return root.val
            root = root.right


if __name__ == '__main__':
    t1 = '5,3,2,$,$,4,$,$,7,6,$,$,8,$,$'
    t1 = deserialize_tree(t1)
    print(find_kth_largest(t1, 3))
