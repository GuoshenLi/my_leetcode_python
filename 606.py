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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(root):
            if not root: return ""
            if not root.left and not root.right: return str(root.val)
            res = str(root.val)

            res += "(" + dfs(root.left) + ")"

            if root.right:
                res += "(" + dfs(root.right) + ")"
            return res

        return dfs(root)
