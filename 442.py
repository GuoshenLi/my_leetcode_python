from collections import Counter
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:


        count_num = Counter(nums)
        res = []
        for k, v in count_num.items():
            if v == 2:
                res.append(k)


        return res

# 与448 几乎一模一样
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        m = len(nums)
        i = 0
        res = []

        while i < m:
            ideal_index = nums[i] - 1
            if nums[i] == nums[ideal_index]:
                i += 1

            elif i == ideal_index:
                i += 1

            elif i != ideal_index:
                nums[i], nums[ideal_index] = nums[ideal_index], nums[i]

        for i in range(m):
            if i != nums[i] - 1:
                res.append(nums[i])

        return res

# 一次遍历 更简单
# 原始数组：[4,3,2,7,8,2,3,1]
# 重置后为：[-4,3,2,-7,8,2,-3,-1]
# 4 代表找到了index为3的数字
# index:  [0,1,2,3,4,5,6,7]
# 代表的数: [1,2,3,4,5,6,7,8,9]
# 如果index代表的数为负数, 则代表它这个位置代表的数出现过

# 遍历一遍
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(index + 1)
            nums[index] = -nums[index]

        return res

print(Solution().findDuplicates(nums = [4,3,2,7,8,2,3,1]))

