def merge_lists(lists: List[ListNode]) -> ListNode:
    if not lists:
        return None

    def merge2lists(l1, l2):
        if l1.val <= l2.val:
            h, p = l1, l1
            l1 = l1.next
        else:
            h, p = l2, l2
            l2 = l2.next
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2= l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return h
    
    l1 = None
    l2 = None
    while len(lists) >= 2:
        while lists and not l1:
            l1 = lists.pop()
        while lists and not l2:
            l2 = lists.pop()
        if l1 and l2:
            lists.append(merge2lists(l1, l2))
        elif l1:
            lists.append(l1)
        elif l2:
            lists.append(l2)
        l1, l2 = None, None
    return lists[0] if lists else None


def merge_lists2(lists):
    d = {}
    for node in lists:
        cur = node
        while cur:
            if cur.val not in d:
                # head, tail
                d[cur.val] = [cur,cur]
            else:
                d[cur.val][1].next = cur
                d[cur.val][1] = cur
            cur = cur.next
        print(d)
    sorted_keys = sorted(list(d.keys()))
    
    for k in range(len(sorted_keys)-1):
        d[sorted_keys[k]][1].next = d[sorted_keys[k+1]][0]
    if sorted_keys:
        return d[sorted_keys[0]][0]
    else:
        return None
