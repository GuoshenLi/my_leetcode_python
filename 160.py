# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        length_A = 0
        length_B = 0
        p = headA
        while p:
            length_A += 1
            p = p.next

        q = headB
        while q:
            length_B += 1
            q = q.next

        step = length_A - length_B

        if step > 0:
            for _ in range(step):
                headA = headA.next

        if step < 0:
            for _ in range(abs(step)):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None
