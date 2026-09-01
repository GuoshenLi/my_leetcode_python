# 暴力法
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []
        for num in nums1:
            index = nums2.index(num)
            while index + 1 <= len(nums2) - 1:
                if nums2[index + 1] > num:
                    res.append(nums2[index + 1])
                    break
                index = index + 1
            else:
                res.append(-1)


        return res




# 单调栈 单调递减栈
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
            维护一个单调递减栈

        '''

        stack = []
        table = {}
        for num in nums2:
            while stack and num > stack[-1]:
                table[stack.pop()] = num
            stack.append(num)
        res = []
        for num in nums1:
            res.append(table[num] if num in table else -1)

        return res