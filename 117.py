from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # 初始化队列同时将第一层节点加入队列中，即根节点

        queue = deque()
        queue.append(root)

        # 外层的 while 循环迭代的是层数
        while queue:
            # 记录当前队列大小
            size = len(queue)
            # 遍历这一层的所有节点
            for i in range(size):
                # 从队首取出元素
                node = queue.popleft()
                # 连接
                if i < size - 1:
                    node.next = queue[0]

                # 拓展下一层节点
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        # 返回根节点
        return root




# O(1)  空间 转化为链表
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        cur = root
        dummy = Node(-1)
        pre = dummy

        while cur:
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next

                if cur.right:
                    pre.next = cur.right
                    pre = pre.next

                cur = cur.next

            cur = dummy.next
            dummy.next = None
            pre = dummy

        return root