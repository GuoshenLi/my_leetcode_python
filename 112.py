# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
# path sum
# 利用两个队列 node_que and sum_que 来储存当前遍历节点和到达节点的路径和
#
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        node_que = deque()
        sum_que = deque()
        node_que.append(root)
        sum_que.append(root.val)

        while node_que:
            node = node_que.popleft()
            sum_node = sum_que.popleft()

            if not node.left and not node.right:
                if sum_node == sum:
                    return True

            if node.left:
                node_que.append(node.left)
                sum_que.append(sum_node + node.left.val)
            if node.right:
                node_que.append(node.right)
                sum_que.append(sum_node + node.right.val)

        return False



# dfs 很巧妙 递归函数作用判断当前节点的值是否等于val（不断递减），依次递归，最终判断叶子节点的值是否最终减少的结果。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return toor.val == sum

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, tempSum):

            if not node: return False
            if not node.left and not node.right: return tempSum + node.val == targetSum

            return dfs(node.left, tempSum + node.val) or dfs(node.right, tempSum + node.val)


        return dfs(root, 0)



