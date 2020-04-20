# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nl = []
        p = head

        while p is not None:
            nl.append(p.val)
            p = p.next

        p1 = len(nl) // 2
        v1 = nl[p1]
        v2 = None

        if p1 != len(nl) - 1:
            v2 = nl[p1 + 1]

        p = head
        while p is not None:
            if v1 == p.val and (v2 == p.next.val if v2 else True):
                return p
            p = p.next
