from utils import construct_linklist, pretty_linklist, ListNode


def delete_node(node: 'ListNode'):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    head = construct_linklist([1, 2, 3])
    print(pretty_linklist(head))
    to_del = head.next.next
    delete_node(to_del)
    print(pretty_linklist(head))

