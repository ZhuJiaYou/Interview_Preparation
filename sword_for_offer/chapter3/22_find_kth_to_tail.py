from utils import construct_linklist


def find_kth_to_tail(head: 'ListNode', k: int) -> 'ListNode':
    p1 = head
    for _ in range(k):
        if p1:
            p1 = p1.next
        else:
            return None
    p2 = head
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2


if __name__ == '__main__':
    l1 = construct_linklist([1, 2, 3, 4, 5])
    print(find_kth_to_tail(l1, 3).val)
