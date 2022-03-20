# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if not inorder and not postorder:
            return None

        root = TreeNode(postorder[-1])
        mid_point = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:mid_point], postorder[:mid_point])
        root.right = self.buildTree(inorder[mid_point + 1:], postorder[mid_point:-1])

        return root