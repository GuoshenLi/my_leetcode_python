# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        last = slow.next
        slow.next = None

        first = self.sortList(head)
        second = self.sortList(last)

        res = self.merge_two_list(first, second)

        return res

    def merge_two_list(self, l1, l2):
        dummy = head = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next

        head.next = l1 or l2
        return dummy.next


