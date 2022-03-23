'''
https://www.acwing.com/problem/content/4/
百度笔试
'''

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

