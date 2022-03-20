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

        # O(n^2)
        # 直接暴力枚举 肯定超时
        # for i in range(low, mid + 1):
        #     for j in range(mid + 1, high + 1):
        #         if nums[i] > 2 * nums[j]:
        #             count += 1


        # O(n)复杂度
        left = low
        right = mid + 1
        while left <= mid:
            while right <= high and nums[left] > 2 * nums[right]:
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


