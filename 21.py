# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(n) 复杂度
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 or l2

        dummy = head = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                head.next = node
                head = head.next
                l1 = l1.next

            else:
                node = ListNode(l2.val)
                head.next = node
                head = head.next
                l2 = l2.next

        if l1:
            head.next = l1

        if l2:
            head.next = l2

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return l1 or l2

        dummy = head = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next

        head.next = l1 or l2

        return dummy.next

