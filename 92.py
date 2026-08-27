# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if m == n:
            return head

        dummy = temp = ListNode(-1, head)

        for i in range(m - 1):
            head = head.next
            temp = temp.next
            # head 去到反转链表的第一个节点
            # temp 去到反转链表的前一个节点

        # 套进去链表反转代码，4行
        p = head
        q = head.next

        for i in range(n - m):
            head.next = q.next
            q.next = p
            p = q
            q = head.next


        # 把temp连上p
        temp.next = p

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        pre = dummy
        cur = head

        for _ in range(left - 1):
            pre = pre.next
            cur = cur.next

        pre.next = self.reverse(cur, right - left)
        return dummy.next

    def reverse(self, head, steps):
        p = head
        q = head.next

        for _ in range(steps):
            head.next = q.next
            q.next = p
            p = q
            q = head.next

        return p




