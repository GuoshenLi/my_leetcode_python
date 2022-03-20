from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while i - q[0][1] >= k:
                # 维持窗口大小为3
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


print(Solution().maxSlidingWindow(nums = [3,1,-1,5], k = 3))