# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         list1 = []
#         while head:
#             list1.append(head.val)
#             head = head.next
#         return self.build_tree(list1)
#
#     def build_tree(self,list_):
#         if not list_:
#             return None
#         mid = len(list_) // 2
#         root = TreeNode(list_[mid])
#         root.left = self.build_tree(list_[:mid])
#         root.right = self.build_tree(list_[mid + 1:])
#
#         return root
#
# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         if not head:
#             return head
#         pre, slow, fast = None, head, head
#
#         while fast and fast.next:
#             fast = fast.next.next
#             pre = slow
#             slow = slow.next
#         if pre:
#             pre.next = None
#
#         next_head = slow.next
#         slow.next = None
#
#         node = TreeNode(slow.val)
#         if slow == fast:
#             return node
#         node.left = self.sortedListToBST(head)
#         node.right = self.sortedListToBST(next_head)
#         return node
#
#
#
# # head 与 node 是不一样的！！！
# # 链表求中点，并且把链表从中间分开！要背下来！
#
# # head 与 node 是不一样的！！！
# # 链表求中点，并且把链表从中间分开！要背下来！
#
# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         if not head:
#             return None
#
#         pre, fast, slow = None, head, head
#         while fast and fast.next:
#             fast = fast.next.next
#             pre = slow
#             slow = slow.next
#
#         node = TreeNode(slow.val)
#         if pre:
#             pre.next = None  #至少两个节点，能分开两个非空的链表
#             head_next = slow.next
#             slow.next = None
#         else:
#             return node
#
#         node.left = self.sortedListToBST(head)
#         node.right = self.sortedListToBST(head_next)
#
#         return node



class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        fast = slow = head
        # 求中点 slow 指向中间往后
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        next_head = slow.next
        pre.next = None
        slow.next = None

        node = TreeNode(slow.val)

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(next_head)

        return node