# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        length = 0
        while head:
            length += 1
            head = head.next


        # 先算长度，再看能够分成几段分别反转，然后套用反转的四行代码
        head = dummy.next
        for i in range(length // k):
            p = head
            q = head.next
            for j in range(k - 1):
                head.next = q.next
                q.next = p
                p = q
                q = head.next

            pre.next = p
            pre = head
            head = q

        return dummy.next



#2022/7/3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        cur = head
        if k == 1: return head

        while cur:
            length += 1
            cur = cur.next

        pre = dummy = ListNode(-1, head)
        cur = head
        times = length // k

        for _ in range(times):
            pre.next = self.reverse_lk(cur, k - 1)
            pre = cur
            cur = cur.next

        return dummy.next


    def reverse_lk(self, head, num):
        p = head
        q = head.next
        for _ in range(num):
            head.next = q.next
            q.next = p
            p = q
            q = head.next

        return p
