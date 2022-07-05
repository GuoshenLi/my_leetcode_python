"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# 不是原地
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        stack = [root]
        res = []

        head = Node(-1)
        cur = head

        while stack:
            stuff = stack.pop()
            if isinstance(stuff, int):
                new_node = Node(stuff)
                cur.right = new_node
                new_node.left = cur
                cur = new_node

            elif isinstance(stuff, Node):
                stack.append(stuff.right)
                stack.append(stuff.val)
                stack.append(stuff.left)

        cur.right = head.right
        head.right.left = cur

        return head.right




class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root: return None

        def dfs(root):
            head = tail = root
            if root.right:
                headR, tail = dfs(root.right)
                root.right = headR
                headR.left = root

            if root.left:
                head, tailL = dfs(root.left)
                root.left = tailL
                tailL.right = root

            return head, tail

        head, tail = dfs(root)
        head.left = tail
        tail.right = head

        return head
