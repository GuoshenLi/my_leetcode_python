class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)
        pre_sum = [0 for i in range(n)]
        post_sum = [0 for i in range(n)]

        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        for i in range(n - 2, -1, -1):
            post_sum[i] = post_sum[i + 1] + nums[i + 1]


        for i in range(n):
            if pre_sum[i] == post_sum[i]:
                return i

        return -1



class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sum_ = 0

        for i in range(len(nums)):
            if 2 * sum_ + nums[i] == total:
                return i

            sum_ += nums[i]

        return -1