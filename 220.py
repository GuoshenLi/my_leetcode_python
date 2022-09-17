class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        k_set = set()
        n = len(nums)

        for i in range(n):
            if t == 0:
                if nums[i] in k_set:
                    return True

            else:
                for item in k_set:
                    if abs(item - nums[i]) <= t:
                        return True

            k_set.add(nums[i])
            if i >= k:
                k_set.remove(nums[i - k])

        return False