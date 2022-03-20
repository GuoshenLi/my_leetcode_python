# 暴力解法 超时
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):

                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False

# 优化之后的暴力 竟然过了
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[j] < nums[k]:
                        return True
        return False


# 双指针
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one = two = float('inf')
        for three in nums:
            if three <= one: one = three
            elif three <= two: two = three
            else: return True
        return False





