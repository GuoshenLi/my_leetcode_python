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

# NC145  01背包
# https://www.nowcoder.com/practice/2820ea076d144b30806e72de5e5d4bbf?tpId=196&difficulty=&judgeStatus=&tags=&title=01&sourceUrl=&gioEnter=menu
#

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算01背包问题的结果
# @param V int整型 背包的体积
# @param n int整型 物品的个数
# @param vw int整型二维数组 第一维度为n,第二维度为2的二维数组,vw[i][0],vw[i][1]分别描述i+1个物品的vi,wi
# @return int整型
#
class Solution:
    def knapsack(self , V: int, n: int, vw: List[List[int]]) -> int:
        # write code here
        dp = [0 for _ in range(V + 1)]


        for item in vw:
            volumn = item[0]
            weight = item[1]
            for i in range(V, -1, -1):
                if i - volumn >= 0:
                    dp[i] = max(dp[i], dp[i - volumn] + weight)

        return dp[-1]


