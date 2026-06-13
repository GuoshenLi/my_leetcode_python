# dp[i][j] 前i个物品 装入容量为j的背包中 能够获得的最大价值
# https://www.acwing.com/problem/content/2/

num_item, capacity = list(map(int, input().split()))
item_list = []

for _ in range(num_item):
    item_list.append(list(map(int, input().split())))


dp = [[0] * (capacity + 1) for i in range(num_item + 1)]


for i in range(1, num_item + 1):
    for j in range(1, capacity + 1):
        capa_this = item_list[i - 1][0]
        value_this = item_list[i - 1][1]

        if j - capa_this >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - capa_this] + value_this)
        else:
            dp[i][j] = dp[i - 1][j]


print(dp[-1][-1])



####### 外循环item数组, 内循环capacity数组

# dp[i][j] 前i个物品 装入容量为j的背包中 能够获得的最大价值

num_item, capacity = list(map(int, input().split()))
item_list = []

for _ in range(num_item):
    item_list.append(list(map(int, input().split())))


dp = [0 for i in range(capacity + 1)]

# 外层循环item lis 内层循环capacity 倒序
for i in range(num_item):
    for j in range(capacity, -1, -1):

        capa_this = item_list[i][0]
        value_this = item_list[i][1]

        if j - capa_this >= 0:
            dp[j] = max(dp[j], dp[j - capa_this] + value_this)


print(dp[-1])

# NC309 如果背包必须要装满 则能装入的最大价值是多少
# https://www.nowcoder.com/practice/3ed13831e2cc4613866edee237d5a804?tpId=196
#

#
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
        for i in range(1, n + 1):
            weight = nums[i - 1][0]
            value = nums[i - 1][1]
            for j in range(1, v + 1):
                if j - weight >= 0:
                    dp[j] = max(dp[j], dp[j - weight] + value)
                    dp_2[j] = max(dp_2[j], dp_2[j - weight] + value)

        return [dp[-1], 0 if dp_2[-1] < 0 else dp_2[-1]]


