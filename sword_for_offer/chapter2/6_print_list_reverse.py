from utils import construct_linklist, ListNode


def print_list_reverse(head: ListNode) -> list:
    stack, h = [], head
    while h:
        stack.append(h.val)
        h = h.next
    return stack[::-1]


if __name__ == '__main__':
    l1 = (1, 2, 3, 4, 5)
    l1 = construct_linklist(l1)
    print(print_list_reverse(l1))
