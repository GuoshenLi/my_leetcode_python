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

# 最右面试题目 回文链表 空间O(1) 时间O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if not head: return True

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_first = self.reverse(slow.next)
        p1 = head
        p2 = second_first
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True

    def reverse(self, head):
        if not head or not head.next: return head
        p = head
        q = head.next
        while q:
            head.next = q.next
            q.next = p
            p = q
            q = head.next

        return p
