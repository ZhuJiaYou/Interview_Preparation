import sys
sys.path.append("..")
from utils import deserialize_tree


def bst2linkedlist(root):
    stack = []
    p = root
    pre = None
    h = None
    while p or stack:
        if p:
            if p.left:
                stack.append(p)
                p = p.left
            else:
                if pre:
                    pre.right = p
                    pre = p
                else:
                    pre = p
                    h = pre
                p = None
        else:
            p = stack.pop()
            if pre:
                pre.right = p
                pre = p
            else:
                pre = p
                h = pre
            p = p.right
    pre = h
    while pre.right:
        pre.right.left = pre
        pre = pre.right

    h.left = None

    return h


if __name__ == '__main__':
    t_str = '10,6,4,$,$,8,$,$,14,12,$,$,16,$,$'
    t1 = deserialize_tree(t_str)
    ans = bst2linkedlist(t1)
    while ans.right:
        print(ans.val, end=' ')
        ans = ans.right
    print(ans.val)
    print()
    while ans.left:
        print(ans.val, end=' ')
        ans = ans.left
    print(ans.val)
