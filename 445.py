# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next

        num2 = 0
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        sum = str(num1 + num2)

        head = dummy = ListNode(-1)
        for digit in sum:
            node = ListNode(digit)
            head.next = node
            head = head.next

        return dummy.next

# 利用栈加头插法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next


        head = None
        carry = 0
        while stack1 and stack2:
            val1 = stack1.pop()
            val2 = stack2.pop()
            digit = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            head = ListNode(digit, head)


        while stack1:
            val1 = stack1.pop()
            digit = (val1 + carry) % 10
            carry = (val1 + carry) // 10

            head = ListNode(digit, head)

        while stack2:
            val2 = stack2.pop()
            digit = (val2 + carry) % 10
            carry = (val2 + carry) // 10

            head = ListNode(digit, head)

        if carry:
            head = ListNode(1, head)

        return head



