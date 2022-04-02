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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        first_lk = head
        second_lk = slow.next
        slow.next = None # 断开

        # 反转一下second_lk
        second_lk = self.reverse_lk(second_lk)

        # 因为是是取中间
        # 因此的话 first_lk 的长度肯定要么等于second_lk的长度
        #                          要吗比second_lk的长度多 1
        dummy = ListNode(-1)
        p = dummy
        while first_lk:
            p.next = first_lk
            first_lk = first_lk.next
            p = p.next

            if second_lk:
                p.next = second_lk
                second_lk = second_lk.next
                p = p.next


        return dummy.next

    def reverse_lk(self, head):
        if not head or not head.next: return head

        p = head
        q = head.next

        while q:
            head.next = q.next
            q.next = p
            p = q
            q = head.next

        return p
