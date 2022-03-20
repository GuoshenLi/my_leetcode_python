from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)

        return self.merge_sort(nums, 0, n - 1)


    def merge_sort(self, nums, left, right):
        if left >= right: return 0
        # 当分出的区间left >= right 的时候 这个区间的逆序对个数为0

        mid = (left + right) // 2
        num_left = self.merge_sort(nums, left, mid)
        num_right = self.merge_sort(nums, mid + 1, right)
        num_cross = self.calculate_between(nums, left, mid, right)
        # 小区间当中逆序对 与小区间之间的逆序对之和
        return num_left + num_right + num_cross


    def calculate_between(self, nums, low, mid, high):
        # 两个有序数组之间的逆序对的个数
        tmp = []
        left = low
        right = mid + 1
        # 区间之间的逆序对的数量
        num_cross = 0

        while left <= mid and right <= high:
            if nums[right] < nums[left]:
                tmp.append(nums[right])
                right += 1
                num_cross += (mid + 1 - left)
            else:
                tmp.append(nums[left])
                left += 1


        while left <= mid:
            tmp.append(nums[left])
            left += 1

        while right <= high:
            tmp.append(nums[right])
            right += 1

        nums[low: high + 1] = tmp

        return num_cross



class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)

        return self.merge_sort(nums, 0, n - 1)


    def merge_sort(self, nums, left, right):
        if left >= right: return 0

        mid = (left + right) // 2
        left_count = self.merge_sort(nums, left, mid)
        right_count = self.merge_sort(nums, mid + 1, right)
        cross_count = self.calculate(nums, left, mid, right)
        return left_count + right_count + cross_count

    def calculate(self, nums, low, mid, high):

        count = 0
        left = low
        right = mid + 1
        # 在分开左右有序数组的时候 已经可以确保 i < j了
        # 因此现在就看nums[i] 是否 > nums[j]

        # 所以先写while循环遍历左有序数组
        while left <= mid:
            while right <= high and nums[left] > nums[right]:
                right += 1

            count += (right - (mid + 1))
            left += 1


        left = low
        right = mid + 1
        tmp = []

        while left <= mid and right <= high:

            if nums[right] < nums[left]:
                tmp.append(nums[right])
                right += 1
            else:
                tmp.append(nums[left])
                left += 1

        while left <= mid:
            tmp.append(nums[left])
            left += 1

        while right <= high:
            tmp.append(nums[right])
            right += 1


        nums[low: high + 1] = tmp


        return count






print(Solution().reversePairs(nums = [7, 5, 6, 4]))