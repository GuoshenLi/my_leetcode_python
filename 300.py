# LSI 死背
# dp问题
from typing import List
class Solution:

    # dp[i] 为以nums[i]为结尾的 最长递增子序列的长度

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# 猿辅导 如果不只是返回长度是要返回子序列要怎么办
# 网易面试题目 字节商业化二面
class Solution:

    # dp[i] 为以nums[i]为结尾的 最长递增子序列的长度

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
        #                           i
        # nums = [2, 1, 5, 3, 6, 4, 8, 9, 7]
        # dp   = [1, 1, 2, 2, 3, 3, 4, 5, 4]
        # res  = [-1,-1,-1,-1,-1]
        #                   j
        length = max(dp)
        res = [-1] * length
        j = length - 1
        for i in range(n - 1, -1, -1):
            if dp[i] == length:
                res[j] = nums[i]
                length -= 1
                j -= 1

        return res


print(Solution().lengthOfLIS(nums = [1,2,8,6,4]))


# 更好的二分问题
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)

        tail = []
        for i in range(size):
            # 【逻辑 1】比 tail 数组实际有效的末尾的那个元素还大
            # 先尝试是否可以接在末尾
            if not tail or nums[i] > tail[-1]:
                tail.append(nums[i])

            else:

                # 使用二分查找法，在有序数组 tail 中
                # 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小
                # 这点很关键！记住这个代码呼之欲出
                left = 0
                right = len(tail) - 1
                while left < right:
                    # 选左中位数不是偶然，而是有原因的，原因请见 LeetCode 第 35 题题解，也是找第一个大于等于它的数的下标
                    mid = (left + right) // 2
                    if tail[mid] < nums[i]:
                        # 中位数肯定不是要找的数，把它写在分支的前面
                        left = mid + 1
                    else:
                        right = mid
                # 走到这里是因为【逻辑 1】的反面，因此一定能找到第 1 个大于等于 nums[i] 的元素，因此无需再单独判断
                tail[left] = nums[i]
                # tail 的长度是对的 但是tail中的内容不是对应的最长子序列
        return len(tail)

