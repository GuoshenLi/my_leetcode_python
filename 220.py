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


'''
把中间的for循环换成二分查找
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        from sortedcontainers import SortedSet
        st = SortedSet()
        left, right = 0, 0
        res = 0
        '''
            nums = [1, 5, 9, 1, 5, 9]
                    [5, 100] # 二分遍历
        '''
        while right < len(nums):
            if right - left > k:
                st.remove(nums[left])
                left += 1
            # 第一个大于等于
            index = bisect.bisect_left(st, nums[right] - t)
            if st and index < len(st) and abs(st[index] - nums[right]) <= t:
                return True
            st.add(nums[right])
            right += 1
        return False
