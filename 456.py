# 132 pattern 倒序 231pattern 顺序遍历（找到次大值）
# 维护一个单调递减栈 （递减）


# stack 当中栈顶的的值比pre_max要大
# 单调递减栈 因此可以把pre_max出栈 因此就可以有2，3pattern 因此再找到一个1即可
from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        pre_max = float('-inf')
        stack = []
        for num in reversed(nums):
            if num < pre_max: return True
            while stack and stack[-1] < num:
                pre_max = stack.pop()
            stack.append(num)

        return False




class Solution:
    # O(n^2)的时间复杂度
    def find132pattern(self, nums: List[int]) -> bool:

        # 先记录1
        n = len(nums)
        min_array = [0 for i in range(n)]
        min_array[0] = nums[0]
        # 从左边来看到当前位置最小的元素
        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])


        for i in range(1, n):
            if nums[i] > min_array[i]:
                for j in range(i + 1, n):
                    if nums[j] > min_array[i] and nums[j] < nums[i]:
                        return True

        return False



Solution().find132pattern(nums = [3,1,4,2])