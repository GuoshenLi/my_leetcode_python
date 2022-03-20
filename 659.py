from typing import List
import collections
# 贪心 越长越好 尽可能添加到已有的子序列后面
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = collections.Counter(nums)
        endMap = collections.Counter()

        for x in nums:
            if countMap[x] > 0:
                if endMap.get(x - 1, 0) > 0:
                    countMap[x] -= 1
                    endMap[x - 1] -= 1
                    endMap[x] += 1

                else:
                    if countMap.get(x + 1, 0) > 0 and countMap.get(x + 2, 0) > 0:
                        countMap[x] -= 1
                        countMap[x + 1] -= 1
                        countMap[x + 2] -= 1
                        endMap[x + 2] += 1
                    else:
                        return False

        return True


import heapq

# 用一个哈希来维护以当前数字num结尾 所对应的子序列的长度
# 如果num - 1存在，则加入所对应的子序列长度最短的序列当中
# 如果没有则另起炉灶
# 最终判断哈希表中是不是所有的长度都大于3

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)

        # 这个哈希表存储的是 key：当前数字结尾，val：子序列的长度
        for x in nums:
            queue = mp[x - 1]
            if queue:
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)

        return all(queue[0] >= 3 for queue in mp.values() if queue)


print(Solution().isPossible([1,2,3,3,4,4,5,5]))