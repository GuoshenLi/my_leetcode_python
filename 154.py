# 与153一样 一直都跟right比较
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1          # 左闭右闭区间，如果用右开区间则不方便判断右值
        while left < right:                     # 循环不变式，如果left == right，则循环结束
            mid = (left + right) // 2           # 地板除，mid更靠近left
            if nums[mid] > nums[right]:         # 中值 > 右值，最小值在右半边，收缩左边界
                left = mid + 1                  # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            elif nums[mid] < nums[right]:       # 明确中值 < 右值，最小值在左半边，收缩右边界
                right = mid                     # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处
            else:                               # 若中间与右边相等，则暴力法，直接right -= 1，背下来
                right -= 1
        return nums[left]                       # 循环结束，left == right，最小值输出nums[left]或nums[right]均可



# # 若求最大值
# # 这个代码也有问题。。。 不要这么搞。。。
# class Solution:
#     def findMin(self, nums):
#         left, right = 0, len(nums) - 1
#         while left < right:
#             mid = (left + right) // 2 # mid靠近left
#             if nums[mid] > nums[left]:
#                 left = mid
#             elif nums[mid] < nums[left]:
#                 right = mid - 1
#             else:
#                 right -= 1
#         return nums[left]

print(Solution().findMin(nums = [3,1,2]))