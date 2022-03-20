from typing import List
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        patches, x = 0, 1
        # x用来维护一个可以到达的数组的右边界
        # 开区间
        length, index = len(nums), 0

        # 如果当前能够到达的范围是[1, x)
        # 那么假如x的话 可以到达的范围就扩充到[1, 2 * x]

        while x <= n:
            if index < length and nums[index] <= x:
                # 就可以用数组中的数字去扩充范围
                # 从而不用额外添加数字
                x += nums[index]
                index += 1
            else:
                # 额外添加数字扩充可以访问的范围
                x *= 2
                patches += 1

        return patches

print(Solution().minPatches(nums = [1,3], n = 6))

