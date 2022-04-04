"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

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


