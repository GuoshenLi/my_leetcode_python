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

# 快排 最坏时间复杂度 O(n ** 2) 看上去本质上是值在交换
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next: return head

        self.quick_sort(head, None)

        return head

    def quick_sort(self, head, end):
        if head != end:
            node = self.partition(head, end)
            self.quick_sort(head, node)
            self.quick_sort(node.next, end)

    def partition(self, head, end):

        p1, p2 = head, head.next

        while p2 != end:
            if p2.val < head.val:
                p1 = p1.next
                p1.val, p2.val = p2.val, p1.val
            p2 = p2.next

        head.val, p1.val = p1.val, head.val

        return p1

