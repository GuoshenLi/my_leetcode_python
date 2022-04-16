# 暴力解法 O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None

        length1 = len(nums1)
        length2 = len(nums2)
        merge = []
        i = j = 0
        while i < length1 and j < length2:
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1

        while i < length1:
            merge.append(nums1[i])
            i += 1
        while j < length2:
            merge.append(nums2[j])
            j += 1
        n = length1 + length2
        if n % 2 == 0:
            return (merge[n // 2] + merge[n // 2 - 1]) / 2
        else:
            return merge[(n - 1) // 2]

# O(log(m + n))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1 = 0
            index2 = 0

            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)

                if nums1[newIndex1] <= nums2[newIndex2]:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1

                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m = len(nums1)
        n = len(nums2)

        total_length = m + n
        if total_length % 2 == 1:
            return getKthElement((total_length + 1) // 2)

        else:
            return (getKthElement(total_length // 2) + getKthElement(total_length // 2 + 1)) / 2





class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(start1, start2, k):


            if start1 == m:
                return nums2[start2 + k - 1]
            if start2 == n:
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])

            newstart1 = min(start1 + k // 2 - 1, m - 1)
            newstart2 = min(start2 + k // 2 - 1, n - 1)

            if nums1[newstart1] <= nums2[newstart2]:
                return getKthElement(newstart1 + 1, start2, k - (newstart1 - start1 + 1))
            else:
                return getKthElement(start1, newstart2 + 1, k - (newstart2 - start2 + 1))

        m = len(nums1)
        n = len(nums2)

        total_length = m + n
        if total_length % 2 == 1:
            return getKthElement(0, 0, total_length // 2 + 1)

        else:
            return (getKthElement(0, 0, total_length // 2) +
                    getKthElement(0, 0, total_length // 2 + 1)) / 2
