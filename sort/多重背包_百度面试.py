'''
https://www.acwing.com/problem/content/4/
百度笔试
'''


# 二维数组
N, V = list(map(int, input().split()))

items = [list(map(int, input().split())) for i in range(N)]

# item[i][0] => v 体积
# item[i][1] => w 价值
# item[i][2] => s 数量

dp = [[0] * (V + 1) for i in range(N + 1)]  # dp[i][j]  items的前i个 背包容量为j的最大体积

for i in range(1, N + 1):
    v, w, s = items[i - 1]
    for j in range(1, V + 1):
        k = 1
        while k <= s and j - k * v >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - k * v] + k * w)
            k += 1
        dp[i][j] = max(dp[i - 1][j], dp[i][j])


print(dp[-1][-1])




# 1维度数组
N, V = list(map(int, input().split()))

items = [list(map(int, input().split())) for i in range(N)]

# item[i][0] => v 体积
# item[i][1] => w 价值
# item[i][2] => s 数量

dp = [0 for i in range(V + 1)]  # dp[i] 表示体积为i的最大价值

for item in items:
    v, w, s = item
    for i in range(V, -1, -1):
        # 选k个
        k = 1
        while i - v * k >= 0 and k <= s:
            dp[i] = max(dp[i], dp[i - v * k] + w * k)

            k += 1



print(dp[-1])

