def remove_nth_from_end(head: 'ListNode', n: int) -> ListNode:
    p1, p2 = head, head
    while n > 0 and p1:
        p1 = p1.next
        n -= 1
    if not p1:
        return head.next
    while p1.next:
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next
    return head


if __name__ == '__main__':


