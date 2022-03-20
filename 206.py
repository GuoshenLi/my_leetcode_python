# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 死背
        if not head: return None
        # p指向反转后的头
        # q指向等待反转的元素
        p = head
        q = head.next

        while q:
            head.next = q.next
            q.next = p
            p = q
            q = head.next

        return p



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        # 链表题目递归出口都这么写

        # 递归版本的话是从最后一个开始反转
        # 一直递归调用以下函数到最后才开始反转
        # 死背
        newHead = self.reverseList(head.next)
        # newHead 是反转后的头节点，永远不变的。


        # 1 -> 2 -> 3 -> 4 -> 5
        # 1 -> 2 -> 3 -> 4 <- 5
        #          head    newHead
                        # original 4.next == None

        head.next.next = head
        head.next = None
        # 1 -> 2 -> 3 <- 4 <-5

        return newHead