# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        head = dummy = ListNode(-1)
        while l1 and l2:
            digit = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            head.next = ListNode(digit)

            head = head.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            digit = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            head.next = ListNode(digit)
            head = head.next
            l1 = l1.next

        while l2:
            digit = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            head.next = ListNode(digit)
            head = head.next
            l2 = l2.next

        if carry:
            head.next = ListNode(1)

        return dummy.next
