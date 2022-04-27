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



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


