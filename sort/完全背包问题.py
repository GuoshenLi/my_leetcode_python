
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





