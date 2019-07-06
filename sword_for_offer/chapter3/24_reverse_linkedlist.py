from utils import construct_linklist, pretty_linklist, ListNode


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


if __name__ == '__main__':
    h1 = construct_linklist([1, 2, 3, 4, 5])
    print(pretty_linklist(h1))
    h2 = reverse_list(h1)
    print(pretty_linklist(h2))
