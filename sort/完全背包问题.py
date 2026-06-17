
# https://www.acwing.com/problem/content/3/

num_item, capacity = list(map(int, input().split()))

num_list = []
for _ in range(num_item):
    num_list.append(list(map(int, input().split())))


dp = [0 for i in range(capacity + 1)]

for j in range(num_item):
    for i in range(1, capacity + 1):
        capa_this = num_list[j][0]
        val_this = num_list[j][1]
        if i - capa_this >= 0:
            dp[i] = max(dp[i], dp[i - capa_this] + val_this)






print(dp[-1])


# NC309 完全背包 https://www.nowcoder.com/practice/3ed13831e2cc4613866edee237d5a804?tpId=196
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param v int整型
# @param n int整型
# @param nums int整型二维数组
# @return int整型一维数组
#
class Solution:
    def knapsack(self, v: int, n: int, nums: List[List[int]]) -> List[int]:
        # write code here

        dp = [0 for _ in range(v + 1)]
        dp_2 = [float("-inf") for _ in range(v + 1)]
        dp_2[0] = 0
        for num in nums:
            weight = num[0]
            value = num[1]
            for j in range(1, v + 1):
                if j - weight >= 0:
                    dp[j] = max(dp[j], dp[j - weight] + value)
                    dp_2[j] = max(dp_2[j], dp_2[j - weight] + value)

        return [dp[-1], 0 if dp_2[-1] < 0 else dp_2[-1]]



