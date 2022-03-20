# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 背诵！！！！
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head == None:
            return None
        dummy, dummy.next = ListNode(-1),head
        pre = dummy
        cur = pre.next
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
                # pre不能动 有可能有连续重复的
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next