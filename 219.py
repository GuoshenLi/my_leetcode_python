class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # 滑动窗口

        window = set()

        for i in range(len(nums)):
            if nums[i] in window: return True

            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k])

        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        '''
            [1, 2, 1, 4, 5, 1, 2, 3, 4]
            维护一个长度为k的窗口　

        '''
        window = set()
        right = 0
        left = 0
        while right < len(nums):
            if right - left > k:
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True

            window.add(nums[right])
            right += 1
        return False

