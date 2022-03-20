# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
###### 对一个树的内部结构进行in-place操作，递归用后序遍历。（与把一棵树展开成链表相对应）
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        node_que = deque()
        node_que.append(root)

        while node_que:
            node = node_que.popleft()
            tmp = node.right
            node.right = node.left
            node.left = tmp
            if node.left:
                node_que.append(node.left)
            if node.right:
                node_que.append(node.right)


        return root
