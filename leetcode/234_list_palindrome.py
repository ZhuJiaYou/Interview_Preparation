# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        if p2:
            p1 = p1.next
        
        pre = None
        nx = None
        while p1:
            nx = p1.next
            p1.next = pre
            pre = p1
            p1 = nx
        
        p2 = head
        while pre:
            if pre.val != p2.val:
                return False
            pre = pre.next
            p2 = p2.next
        return True
