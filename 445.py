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

        carry = 0
        head = None #  头插法可以直接初始化head = None
        while stack1 and stack2:
            digit1 = stack1.pop()
            digit2 = stack2.pop()
            digit = (carry + digit1 + digit2) % 10
            carry = (carry + digit1 + digit2) // 10

            node = ListNode(digit)
            node.next = head
            head = node

        while stack1:
            digit1 = stack1.pop()
            digit = (carry + digit1) % 10
            carry = (carry + digit1) // 10

            node = ListNode(digit)
            node.next = head
            head = node

        while stack2:
            digit2 = stack2.pop()
            digit = (carry + digit2) % 10
            carry = (carry + digit2) // 10

            node = ListNode(digit)
            node.next = head
            head = node

        if carry:
            node = ListNode(1)
            node.next = head
            head = node
        return head