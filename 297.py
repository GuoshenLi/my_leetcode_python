# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 如果树的节点值是唯一的，那么是不是还可以借助前序+中序遍历，因为前序+中序遍历可以确定一棵树~。。。
# 前提是树的节点唯一
# 递归

class Codec:

    def serialize(self, root):
        if not root: return 'None'

        return str(root.val) + ' ' + self.serialize(root.left) + ' ' + self.serialize(root.right)


    def deserialize(self, data):
        li = data.split()


        def build_tree(li):
            if not li: return None
            val = li.pop(0)
            if val == 'None': return None

            root = TreeNode(val)
            root.left = build_tree(li)
            root.right = build_tree(li)
            return root

        return build_tree(li)



# 非递归
from collections import deque
class Codec:

    def serialize(self, root):

        s = ""
        queue = deque()
        queue.append(root)
        while queue:
            root = queue.popleft()
            if root:
                s += str(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                s += "None"
            s += " "
        return s

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += '#'
            else:
                res += str(node.val)
                queue.append(node.left)
                queue.append(node.right)

            res += ' '
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data[0] == '#': return None
        data = data.split()
        root = TreeNode(data[0])
        queue = deque()
        queue.append(root)
        i = 1

        while queue:
            node = queue.popleft()

            val = data[i]
            if val != '#':
                node.left = TreeNode(val)
                queue.append(node.left)

            val = data[i + 1]
            if val != '#':
                node.right = TreeNode(val)
                queue.append(node.right)

            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))