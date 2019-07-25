from utils import ListNode, pretty_linklist


class RandomListNode(ListNode):
    def __init__(self, x):
        super().__init__(x)
        self.random = None


def copyRandomList(head: 'RandomListNode') -> 'RandomListNode':
    """
    解法1：遍历两次
    """
    cp_map = {}

    m = n = head
    while m:
        cp_map[m] = RandomListNode(m.val)
        m = m.next
    while n:
        cp_map[n].next = cp_map.get(n.next)
        cp_map[n].random = cp_map.get(n.random)
        n = n.next

    return cp_map.get(head)


def copyRandomList2(head: 'RandomListNode') -> 'RandomListNode':
    """
    解法2：遍历一次
    """
    from collections import defaultdict
    cp = defaultdict(lambda: RandomListNode(0))
    cp[None] = None
    n = head
    while n:
        cp[n].val = n.val
        cp[n].next = cp[n.next]
        cp[n].random = cp[n.random]
        n = n.next
    return cp[head]


if __name__ == '__main__':

