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


