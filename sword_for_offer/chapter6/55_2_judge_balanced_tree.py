import sys
sys.path.append("..")
from collections import defaultdict
from utils import TreeNode, deserialize_tree


def is_balanced(root):
    stack = []
    last = None
    node = root
    depths = defaultdict(int)
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right = depths[node.left], depths[node.right]
                if abs(left - right) > 1:
                    return False
                depths[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True



if __name__ == '__main__':
    t1 = '1,2,4,$,$,5,7,$,$,$,3,$,6,$,$'
    t1 = deserialize_tree(t1)
    print(is_balanced(t1))
    t2 = '1,2,4,$,$,5,7,8,$,$,$,$,3,$,6,$,$'
    t2 = deserialize_tree(t2)
    print(is_balanced(t2))
