class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        match = [-1] * n

        def dfs(u, visited):

            for v in range(n):
                if visited[v] == False and grid[u][v] == 1:
                    # 有边存在 并且 u所连接的v没有访问过

                    visited[v] = True

                    if match[v] == -1 or dfs(match[v], visited):
                        # 这个女生没有被匹配 或者 ！！！ 关键
                        # 这个女生所对应的男生可以换一个
                        '''
                            If job v is not assigned to an applicant or previously assigned applicant for job v (match[v] has an alternate job available) !!!
                        '''
                        match[v] = u
                        return True

            return False

        res = 0
        for i in range(m):
            visited = [False] * n
            if dfs(i, visited):
                res += 1

        return res