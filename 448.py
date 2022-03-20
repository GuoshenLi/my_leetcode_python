# 与442 几乎一模一样

# 一次遍历 更简单
# 原始数组：[4,3,2,7,8,2,3,1]
# 重置后为：[-4,-3,-2,-7,8,2,-3,-1]
# index:  [0,1,2,3,4,5,6,7]
# 代表的数: [1,2,3,4,5,6,7,8,9]
# 如果index代表的数为负数, 则代表它这个位置代表的数出现过

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        res = []
        for i in range(len(nums)):

            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = - nums[index]

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)


        return res