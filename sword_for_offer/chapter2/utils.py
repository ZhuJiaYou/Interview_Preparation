class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


def construct_linklist(nodes: 'iterable') -> 'LinkedList':  # NOQA
    vals = list(nodes)
    head = ListNode(0)
    h = head
    for val in vals:
        h.next = ListNode(val)
        h = h.next
    return head.next


def preorder_traversal(root: TreeNode) -> list:
    def dfs(node):
        if node:
            yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)

    return list(dfs(root))


def inorder_traversal(root: TreeNode) -> list:
    def dfs(node):
        if node:
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)

    return list(dfs(root))
