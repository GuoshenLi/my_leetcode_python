# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        val = max(nums)
        idx = nums.index(val)
        root = TreeNode(val)

        root.left = self.constructMaximumBinaryTree(nums[0: idx])
        root.right = self.constructMaximumBinaryTree(nums[idx + 1:])

        return root
