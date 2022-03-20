class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        sort = []
        index1 = 0
        index2 = 0
        while index1 < m and index2 < n:
            if nums1[index1] <= nums2[index2]:
                sort.append(nums1[index1])
                index1 += 1
            else:
                sort.append(nums2[index2])
                index2 += 1
        while index1 < m:
            sort.append(nums1[index1])
            index1 += 1

        while index2 < n:
            sort.append(nums2[index2])
            index2 += 1

        nums1[:] = sort



