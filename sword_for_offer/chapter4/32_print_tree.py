from utils import deserialize_tree



def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
    ans, level = [], root and [root]
    while level:
        ans.append([n.val for n in level])
        tmp = level
        level = []
        for n in tmp:
            level += [k for k in (n.left, n.right) if k]
    return ans
