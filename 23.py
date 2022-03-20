# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 用堆去做（优先队列）

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next

        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next






# 2021.8.11
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None

        dummy = ListNode(-1)
        pre = dummy
        node_val_list = [[lists[i].val, i] for i in range(len(lists))if lists[i]]
        heapq.heapify(node_val_list)

        while node_val_list:
            _, i = heapq.heappop(node_val_list)
            pre.next = lists[i]
            pre = pre.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(node_val_list, [lists[i].val, i])

        return dummy.next