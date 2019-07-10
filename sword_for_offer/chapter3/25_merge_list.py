from utils import ListNode, construct_linklist, pretty_linklist


def merge_two_lists(l1, l2):
    l = head = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            l.next, l1 = l1, l1.next
        else:
            l.next, l2 = l2, l2.next
        l = l.next
    l.next = l1 or l2
    return head.next


if __name__ == '__main__':
    h1 = construct_linklist([1, 2, 4])
    h2 = construct_linklist([1, 3, 4])
    print(pretty_linklist(merge_two_lists(h1, h2)))
