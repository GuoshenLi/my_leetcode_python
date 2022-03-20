# 3sum 排序加双指针
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        dis = float('+inf')

        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if abs(sum3 - target) < dis:
                    dis = abs(sum3 - target)
                    closest = sum3
                if sum3 < target:
                    left += 1
                elif sum3 > target:
                    right -= 1
                else:
                    return sum3

        return closest
