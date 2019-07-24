import sys
sys.path.append("..")
from utils import deserialize_tree


def bitree_path_sum(root, s):
    path = 0
    p = root
    rights_and_path = []
    results = []
    result = []
    while p or rights_and_path:
        if p:
            path += p.val
            result.append(p.val)
            if p.left is None and p.right is None and path == s:
                results.append(result)
                p = None
            elif p.left and p.right:
                rights_and_path.append((p.right, path, result[:]))
                p = p.left
            elif p.left and (not p.right):
                p = p.left
            elif p.right and (not p.left):
                rights_and_path.append((p.right, path, result[:]))
                p = None
            elif p.left is None and p.right is None:
                p = None
        else:
            p, path, result = rights_and_path.pop()
    return results


if __name__ == '__main__':
    t1 = '10,5,4,$,$,7,$,$,12,$,$'
    t1 = deserialize_tree(t1)
    print(bitree_path_sum(t1, 22))
