# 使用贪心思想扩展数对链，在所有可作为下一个数对的集合中选择第二个数最小的数对添加到数对链。
# 根据思路中的描述，按照数对第二个数的升序序列遍历所有数对，如果当前数对可以加入链，则加入。
# 贪心

class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key = lambda x: x[1])
        cur, ans = float('-inf'), 0
        for x, y in pairs:
            if cur < x:
                cur = y
                ans += 1
        return ans



class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        # 有点像最长递增子序列
        pairs.sort()

        dp = [1 for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


