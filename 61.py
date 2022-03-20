# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        length = 0
        p = head
        dummy = ListNode(-1)
        dummy.next = head
        while p:
            length += 1
            p = p.next

        k = k % length

        if k == 0:
            return head

        p = dummy
        for i in range(length - k):
            p = p.next

        q = p.next
        dummy.next = q
        p.next = None

        while q.next:
            q = q.next
        q.next = head

        return dummy.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        length = 0
        cur = head
        tail = head
        while cur:
            length += 1
            cur = cur.next
            if tail.next:
                tail = tail.next

        k = k % length

        if k == 0: return head

        # 其实就是倒数第几个
        dummy = ListNode(-1, head)
        pre = dummy
        cur = head

        for i in range(length - k - 1):
            cur = cur.next

        pre.next = cur.next
        cur.next = None

        tail.next = head

        return dummy.next













