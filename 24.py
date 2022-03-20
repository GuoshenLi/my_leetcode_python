# 2022.1.27
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        dummy = ListNode(-1, head)
        pre = dummy
        cur = head
        while cur and cur.next:
            temp = cur.next
            pre.next = temp
            cur.next = temp.next
            temp.next = cur

            pre = cur
            cur = cur.next

        return dummy.next
