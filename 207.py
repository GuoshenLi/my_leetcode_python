# 广度优先搜索
from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        in_deg = [0 for _ in range(numCourses)]

        for k, v in prerequisites:
            graph[v].append(k)
            in_deg[k] += 1

        queue = deque([i for i in range(numCourses) if not in_deg[i]])
        visited = 0
        while queue:
            visited += 1
            course = queue.popleft()
            for item in graph[course]:

                in_deg[item] -= 1

                if in_deg[item] == 0:
                    queue.append(item)
        print(in_deg)
        return visited == numCourses



# 背！深度优先搜索！
# 要有一个标志位为 0，1，-1
# 0为还没有被访问
# -1为已经完成访问，输入到栈中的节点
# 1为正在被此次dfs访问，在路径上的节点（看是否有环）
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        # 按顺序从每一门课发起深度优先搜索
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True

