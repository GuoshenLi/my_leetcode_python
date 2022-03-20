class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [-1] * n
        stack = []
        # 跟i相关的都要除以n
        for i in range(2 * n - 1):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                res[idx] = nums[i % n]
            stack.append(i % n)

        return res