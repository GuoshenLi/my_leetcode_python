# 最小生成树 prim 算法 模版


n, m = list(map(int, input().split()))
# n个点, m条约束

in_MST = [False] * n
min_dis = [float('+inf')] * n
min_dis_parent = [None] * n

dis_graph = [[float('+inf')] * n for i in range(n)]
for i in range(m):
    i, j, w = list(map(int, input().split()))
    dis_graph[i][j] = w
    dis_graph[j][i] = w

# 从结点0开始
# 初始化
in_MST[0] = True
res = 0

for i in range(1, n):
    min_dis[i] = dis_graph[0][i]
    if min_dis[i] != float('+inf'):
        min_dis_parent[i] = 0

for _ in range(1, n):
    min_val = float('+inf')
    for j in range(n):
        if not in_MST[j] and min_dis[j] < min_val:
            min_index = j
            min_val = min_dis[j]

    res += min_val
    in_MST[min_index] = True
    print(min_dis_parent[min_index], min_index)  # print out all the tree

    for j in range(n):
        if not in_MST[j] and dis_graph[j][min_index] < min_dis[j]:
            min_dis[j] = dis_graph[j][min_index]
            min_dis_parent[j] = min_index

print(res)


# test case
# 9 14
# 0 1 4
# 1 2 8
# 2 3 7
# 3 4 9
# 4 5 10
# 3 5 14
# 2 5 4
# 5 6 2
# 6 8 6
# 2 8 2
# 6 7 1
# 7 8 7
# 1 7 11
# 0 7 8