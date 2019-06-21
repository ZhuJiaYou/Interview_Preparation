class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


def construct_linklist(nodes: 'iterable') -> 'LinkedList':  # NOQA
    vals = list(nodes)
    head = ListNode(0)
    h = head
    for val in vals:
        h.next = ListNode(val)
        h = h.next
    return head.next
