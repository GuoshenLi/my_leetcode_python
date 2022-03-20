# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            True
        stack = []

        slow = fast = head

        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        if fast:  # 如果长度为奇数
            slow = slow.next

        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        return True