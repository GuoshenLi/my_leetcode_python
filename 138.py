

# hasp table!
# 只有有随机指针的链表才会问深拷贝，否则直接后插即可
# 深拷贝指的是每一个节点都要new 一个 Node
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return None
        self.visited = {None:None}
        tmp = head
        while tmp:
            self.visited[tmp] = Node(tmp.val, None, None)
            tmp = tmp.next
        new_head = new_node = self.visited[head]
        while head:
            new_node.next = self.visited[head.next]
            new_node.random = self.visited[head.random]
            new_node = new_node.next
            head = head.next
        return new_head