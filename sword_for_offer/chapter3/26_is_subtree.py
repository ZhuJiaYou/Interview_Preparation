from utils import TreeNode, deserialize_tree


def is_subtree(s: 'TreeNode', t: 'TreeNode') -> 'bool':
    def is_same(a):
        p1 = a
        p2 = t
        rights_t = []
        rights_a = []
        while (p2 or rights_t) and (p1 or rights_a):
            if p2:
                if not p1 or p1.val != p2.val:
                    return False
                rights_t.append(p2.right)
                p2 = p2.left
                rights_a.append(p1.right)
                p1 = p1.left
            else:
                p2 = rights_t.pop()
                p1 = rights_a.pop()
        if p2 or rights_t:
            return False
        return True

    p = s
    rights = []
    result = False
    while p or rights:
        if p:
            if p.val == t.val:
                result = is_same(p)
                if result:
                    return True
            rights.append(p.right)
            p = p.left
        else:
            p = rights.pop()
    return result


if __name__ == '__main__':
    t1 = '8,8,9,$,$,2,4,$,$,7,$,$,7,$,$'
    t1 = deserialize_tree(t1)
    t2 = '8,9,$,$,2,$,$'
    t2 = deserialize_tree(t2)
    print(is_subtree(t1, t2))

    t1 = TreeNode(1)
    t1.left, t1.right = TreeNode(2), TreeNode(3)
    t1.left.left = TreeNode(4)
    t2 = TreeNode(2)
    t2.left = TreeNode(5)
    print(is_subtree(t1, t2))
