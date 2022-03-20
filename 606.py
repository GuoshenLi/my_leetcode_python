# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 题目的意思是子节点需要用()来包裹。
# 举例来说，二叉树[root,left,right]，则转换为root(left)(right)。
# 如果只有left为空节点，则输出root()(right)；
# 如果只有right为空节点则可以忽略右节点的()，输出为root(left)。
# 其实就是先序遍历
class Solution:
    def tree2str(self, t: TreeNode) -> str:

        def dfs(node):
            if not node:
                return ''

            if not node.left and not node.right:
                return str(node.val)

            res = str(node.val)

            if node.left:
                res += '(' + dfs(node.left) + ')'

            else:
                res += '()'

            if node.right:
                res += '(' + dfs(node.right) + ')'

            return res

        return dfs(t)


