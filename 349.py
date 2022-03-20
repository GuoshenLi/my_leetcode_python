class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        inter = []

        for item in nums1:
            if item in nums2:
                inter.append(item)

        return set(inter)



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return list(set(nums1) & set(nums2))