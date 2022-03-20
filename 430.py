"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# 递归
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        head, back = self.dfs(head)
        return head

    def dfs(self, head):
        if not head: return None
        cur = head

        while cur:
            if cur.child:
                next_node = cur.next
                # 一定要分类讨论
                if next_node:
                    node, tail = self.dfs(cur.child)

                    cur.next = node
                    node.prev = cur

                    tail.next = next_node
                    next_node.prev = tail

                    cur.child = None
                    cur = tail
                else:
                    node, tail = self.dfs(cur.child)

                    cur.next = node
                    node.prev = cur

                    cur.child = None
                    cur = tail
            if not cur.next:
                tail = cur

            cur = cur.next

        return head, tail

