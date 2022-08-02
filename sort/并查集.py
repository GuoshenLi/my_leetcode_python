# 判断无向图有没有环


def union_vertices(x, y):
    x_root = find_root(x)
    y_root = find_root(y)
    if x_root == y_root: return False
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1
    return True

def find_root(x):
    while parent[x] != -1:
        x = parent[x]
    return x

edges = [[0, 1], [1, 2], [1, 3], [3, 4], [2, 3]]
n = 5
parent = [-1] * n
rank = [0] * n
for x, y in edges:
    if not union_vertices(x, y):
        print("has cycle!")
