from utils import construct_linklist, pretty_linklist, ListNode


def sort_list(head):
    def partition(start, end):
        node = start.next.next  # node to iterate
        first_pivot = start.next
        first_pivot.next = end  # Insert large node between pivot and end
        last_pivot = first_pivot
        while node != end:
            tmp = node.next
            if node.val > first_pivot.val:
                node.next = last_pivot.next
                last_pivot.next = node
            elif node.val < first_pivot.val:
                node.next = start.next
                start.next = node
            else:
                node.next = last_pivot.next
                last_pivot.next = node
                last_pivot = last_pivot.next
            node = tmp
        return [first_pivot, last_pivot]

    def qsort(start, end):
        if start.next != end:
            first_pivot, last_pivot = partition(start, end)
            qsort(start, first_pivot)
            qsort(last_pivot, end)

    head_pre = ListNode(0)
    head_pre.next = head
    qsort(head_pre, None)
    return head_pre.next


if __name__ == '__main__':
     l1 = construct_linklist([4, 2, 1, 3])
     l1 = sort_list(l1)
     print(pretty_linklist(l1))
