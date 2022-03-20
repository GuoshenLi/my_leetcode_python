# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        more = more_dummy = ListNode(0)
        less = less_dummy = ListNode(0)

        while head:
            if head.val >= x:
                more.next = head
                more = more.next

            else:
                less.next = head
                less = less.next

            head = head.next
        more.next = None
        less.next = more_dummy.next

        return less_dummy.next
