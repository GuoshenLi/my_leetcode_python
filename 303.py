# 重复调用 暴力解法 很慢
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        if not self.nums:
            return 0
        else:
            sum = 0

            for index in range(i, j + 1):
                sum += self.nums[index]
            return sum
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)





# 最优解法 前缀和
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_sum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.pre_sum[i + 1] = self.pre_sum[i] + self.nums[i]
        print(self.pre_sum)

    def sumRange(self, i: int, j: int) -> int:
        if not self.nums:
            return 0
        else:
            return self.pre_sum[j + 1] - self.pre_sum[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)