"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = []

        def recur(node):
            if node:
                for sub_node in node.children:
                    recur(sub_node)
                res.append(node.val)

        recur(root)
        return res


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 同样染色法 死背
class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        stack = [root]
        res = []

        while stack:
            tmp = stack.pop()
            if isinstance(tmp, Node):
                stack.append(tmp.val)
                for sub_node in tmp.children[::-1]:
                    stack.append(sub_node)

            elif isinstance(tmp, int):
                res.append(tmp)

            else:
                continue


        return res




