# 我们遍历该数组两次，处理出每一个学生分别满足左规则或右规则时，最少需要被分得的糖果数量。
# 每个人最终分得的糖果数量即为这两个数量的最大值。

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 山峰问题

        n = len(ratings)
        for_ward = [1] * n
        back_ward = [1] * n
        res = 0

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                for_ward[i] = for_ward[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                back_ward[i] = back_ward[i + 1] + 1

        for i in range(n):
            res += max(for_ward[i], back_ward[i])


        return res
