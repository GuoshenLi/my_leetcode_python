# 判断是不是三角形 三条边分别判断两边之和是否大于第三遍即可 不用判断两边之差
# 竟然通过218 / 220
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):


                    if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                        count += 1
        return count

# 三条边能够成三角形的充分必要条件是：
#较短的两边之和大于（不包括等于）第三边（最长边）。

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 索引数组：[0, 1, 2, 3, 4]，size = 5
        # i 最多到倒数第 2 个索引

        size = len(nums)

        # 思路 1：从前到后，先固定 i ，再固定 j ，最后确定 k 的范围
        # 首先不要忘记排序
        nums.sort()
        res = 0

        # 注意边界，看上面那个索引数组知道 i 最多取到 2
        for i in range(size):
            # 要给 k 留一个位置，故 size - 1 是上限（取不到）
            for j in range(i + 1, size):
                # 在区间 [j + 1, size - 1] 中找第 1 个不能构成三角形的数
                # k 与 j 之间的数的个数就是一票解
                # 等价于，在子区间 [j + 1, size - 1] 里找第 1 个大于等于 nums[i] + nums[j] 的数
                k = self.__find_first_cannot_triangle(nums, j + 1, size - 1, nums[i] + nums[j])
                if k == -1:
                    # 说明子区间 [j + 1, size - 1] 全部的数都可以构成三角形
                    # 其中的数的个数为 size - 1 - (j + 1) + 1
                    res += (size - j - 1)
                else:
                    # 说明子区间 [j + 1, k) 全部的数可以构成三角形，注意：这里 k 取不到
                    # 其中的数的个数为 k - (j + 1)
                    res += (k - j - 1)
        return res
    # 找第一个大于等于target的数 套路 所以先判断小于
    def __find_first_cannot_triangle(self, nums, left, right, target):
        # 在 nums 的子区间 [left, right] 里找第 1 个大于等于 target 的元素的索引
        # 如果不存在，返回 -1
        if target > nums[-1]:
            return -1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
