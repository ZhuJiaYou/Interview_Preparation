from utils import ListNode, construct_linklist


def detect_cycle(head: 'ListNode') -> 'ListNode':
    fast = slow = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break
    else:
        return None

    h = head
    while h is not slow:
        h, slow = h.next, slow.next
    return h


if __name__ == '__main__':
    h1 = construct_linklist([1, 2, 3, 4, 5, 6])
    h1.next.next.next.next.next.next = h1.next.next
    print(detect_cycle(h1).val)
