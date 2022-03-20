"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 参考二叉树的先序遍历
class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        res = []

        def recur(node):
            if node:
                res.append(node.val)
                for sub_node in node.children:
                    recur(sub_node)

        recur(root)
        return res

# 迭代 染色法
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            stuff = stack.pop()

            if isinstance(stuff, Node):
                for sub_node in stuff.children[::-1]:
                    stack.append(sub_node)
                stack.append(stuff.val)

            elif isinstance(stuff, int):
                res.append(stuff)

            else:
                continue

        return res



