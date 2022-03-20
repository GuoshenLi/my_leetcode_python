class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    res = max(res, nums[i] * nums[j] * nums[k])

        return res





# 思想很重要 以前的题目也有过 如何求一个数组中的最小两个数和最大三个数
# 不用排序 设置多个指针，然后不断移动 判断的时候先判断 是否比最小的小 然后判断是否比最大的大

# 如果数组中全是非负数，则排序后最大的三个数相乘即为最大乘积；如果全是非正数，则最大的三个数相乘同样也为最大乘积。
# 如果数组中有正数有负数，则最大乘积既可能是三个最大正数的乘积，也可能是两个最小负数（即绝对值最大）与最大正数的乘积。
# 综上，我们在给数组排序后，分别求出三个最大正数的乘积，以及两个最小负数与最大正数的乘积，二者之间的最大值即为所求答案。



class Solution(object):
    def maximumProduct(self, nums):

        # 求出最小的两个数 和 最大的三个数


        min1 = float('+inf')
        min2 = float('+inf')

        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')


        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num

            elif num < min2:
                min2 = num

            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num

            elif num > max2:
                max3 = max2
                max2 = num

            elif num > max3:
                max3 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)



