class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        k_set = set()

        for i in range(len(nums)):
            if t == 0:
                if nums[i] in k_set:
                    return True

                # 不加判断会超时
            else:
                for item in k_set:
                    if abs(item - nums[i]) <= t:
                        return True

            k_set.add(nums[i])

            if len(k_set) == k + 1:
                k_set.remove(nums[i - k])

        return False
