# 深度优先搜索
from collections import defaultdict
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjacent = defaultdict(list)
        flags = [0 for i in range(numCourses)]

        for cur, pre in prerequisites:
            adjacent[pre].append(cur)

        res = []

        def dfs(i):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacent[i]:
                if not dfs(j): return False
            flags[i] = -1
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res[::-1]


print(Solution().findOrder(numCourses=5,
                     prerequisites=[[3, 0], [1, 0], [3, 1], [2, 1], [4, 3], [4, 2]]))






from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjacent = defaultdict(list)
        # key: 先修课，key: 后续课程
        in_deg = [0 for i in range(numCourses)]
        res = []

        for cur, pre in prerequisites:
            adjacent[pre].append(cur)
            in_deg[cur] += 1

        queue = deque([i for i in range(numCourses) if not in_deg[i]])
        while queue:
            node = queue.popleft()
            res.append(node)
            for item in adjacent[node]:
                in_deg[item] -= 1
                if in_deg[item] == 0:
                    queue.append(item)

        if len(res) == numCourses:
            return res

        else:
            return []