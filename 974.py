from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        pre_sum = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]


        table = defaultdict(int)
        table[0] = 1

        res = 0
        for j in range(1, n + 1):
            if pre_sum[j] % k in table:
                res += table[pre_sum[j] % k]

            table[pre_sum[j] % k] += 1


        return res



