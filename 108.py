# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None

        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, left, right):
        if left > right: return None
        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, left, mid - 1)
        root.right = self.dfs(nums, mid + 1, right)

        return root