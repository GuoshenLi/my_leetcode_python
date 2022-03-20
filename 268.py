class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        num_list = [0 for _ in range(n + 1)]
        for item in nums:
            num_list[item] += 1

        for i in range(n + 1):
            if num_list[i] == 0:
                return i



# 时间O(n) 空间O(1) 求和再减
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# 时间O(n) 空间O(1) 考异或运算
class Solution:
    def missingNumber(self, nums):
        # 若两个相同，则异或为0.考异或运算.
        xor = 0
        for i in range(len(nums) + 1):
            xor = xor ^ i

        for item in nums:
            xor = xor ^ item

        return xor