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

        dict1 = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                cur = stack.pop()
                dict1[cur] = num
            stack.append(num)

        for item in stack:
            dict1[item] = -1

        return [dict1[item] for item in nums1]
