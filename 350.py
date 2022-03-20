# 350 数组无序的情况下
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)

        res = []
        for item in nums1:
            if item in nums2:
                count = min(nums1[item], nums2[item])
                res.extend([item] * count)

        # return (nums1 & nums2).elements() counter才有elements 才可以 &操作
        return res


from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 排序版本
        # follow up

        nums1.sort()
        nums2.sort()

        length1 = len(nums1)
        length2 = len(nums2)

        pointer1, pointer2 = 0, 0
        res = []
        while pointer1 <= length1 - 1 and pointer2 <= length2 - 1:
            if nums1[pointer1] == nums2[pointer2]:
                res.append(nums1[pointer1])
                pointer1 += 1
                pointer2 += 1

            elif nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1

            elif nums1[pointer1] > nums2[pointer2]:
                pointer2 += 1

        return res
