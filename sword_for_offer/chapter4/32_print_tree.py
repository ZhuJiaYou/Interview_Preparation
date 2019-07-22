import sys
sys.path.append("..")
from utils import deserialize_tree


def level_order_no_sep(root):
    if not root:
        return []
    level = [root]
    ans = []
    while level:
        tmp = level
        level = []
        for node in tmp:
            ans.append(node.val)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
    return ans



def level_order_sep(root: 'TreeNode') -> 'List[List[int]]':
    ans, level = [], root and [root]
    while level:
        ans.append([n.val for n in level])
        tmp = level
        level = []
        for n in tmp:
            level += [k for k in (n.left, n.right) if k]
    return ans


def level_order_zigzag(root: 'TreeNode') -> 'List[List[int]]':
    ans, level = [], root and [root]
    r = False
    while level:
        if r:
            ans.append([n.val for n in level[::-1]])
            r = False
        else:
            ans.append([n.val for n in level])
            r = True
        tmp = level
        level = []
        for n in tmp:
            level += [k for k in (n.left, n.right) if k]
    return ans



if __name__ == '__main__':
    t1 = '8,6,5,$,$,7,$,$,10,9,$,$,11,$,$'
    t1 = deserialize_tree(t1)
    print(level_order_sep(t1))
    print(level_order_no_sep(t1))
    print(level_order_zigzag(t1))
