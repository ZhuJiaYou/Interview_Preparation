import sys
sys.path.append("..")
from utils import construct_linklist


def get_intersection(h1, h2):
    p1, p2 = h1, h2
    while p1 is not p2:
        # NOTICE THE BUG
        # p1 = p1.next if p1.next else h2
        # p2 = p2.next if p2.next else h1
        p1 = p1.next if p1 else h2
        p2 = p2.next if p2 else h1
    return p1


if __name__ == '__main__':
    h1 = construct_linklist([4, 2, 1, 5, 5, 7])
    h2 = construct_linklist([8, 3])
    h2.next.next = h1.next.next
    intersection = h1.next.next
    print(intersection is get_intersection(h1, h2))

    h1 = construct_linklist([4, 2, 1, 5, 5, 7])
    h2 = construct_linklist([8, 3])
    print(get_intersection(h1, h2))
