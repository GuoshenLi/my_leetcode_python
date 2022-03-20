# 暴力解法

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # 判断x和x+1构成和谐子序列 不用反过来看x和x-1因为会重复
        res = 0
        for i in range(len(nums)):
            count1 = 0
            count2 = 0
            for j in range(len(nums)):

                if nums[i] == nums[j]:
                    count1 += 1
                elif nums[i] == nums[j] + 1:
                    count2 += 1

                if count1 and count2:
                    res = max(res, count1 + count2)
        return res

# 建立哈希表 通过
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:

        count = Counter(nums)
        res = 0
        for item in count.keys():
            if item + 1 in count:

                res = max(res, count[item] + count[item + 1])

        return res