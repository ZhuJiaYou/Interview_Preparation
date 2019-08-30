from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    level_end = 1
    traverse_end = 1
    que = deque([root]) if root else deque()
    i = 1
    p = None
    while que:
        p = que.popleft()
        if i != traverse_end:
            p.next = que[0]
        else:
            level_end *= 2
            traverse_end += level_end
        if p.left:
            que.append(p.left)
            que.append(p.right)
        i += 1
    return root
