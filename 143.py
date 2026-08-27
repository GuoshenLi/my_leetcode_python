# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return None
        # 下面这两行语句 找中间节点 当为链表长度偶数的时候 要思考中间节点为中间的前一个还是后一个
        # 这里用前一个比较方便，因此fast初始化为head.next
        slow = head
        fast = head.next
        p1 = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        p2_head = slow.next
        slow.next = None

        p = p2_head
        q = p2_head.next

        while q:
            p2_head.next = q.next
            q.next = p
            p = q
            q = p2_head.next

        p2 = p
        temp = head

        #  p1 p2 为等待链接的那两个链表的头，用temp做中间媒介
        while p2:
            p1 = p1.next
            temp.next = p2
            temp = temp.next

            p2 = p2.next
            temp.next = p1
            temp = temp.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        if not head.next: return head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None
        second_head = self.reverse(second_head)

        cur = dummy = ListNode(-1)
        while head and second_head:
            cur.next = head
            head = head.next
            cur = cur.next

            cur.next = second_head
            second_head = second_head.next
            cur = cur.next
        cur.next = head or second_head

        return dummy.next

    def reverse(self, head):

        p = head
        q = head.next

        while q:
            head.next = q.next
            q.next = p
            p = q
            q = head.next

        return p