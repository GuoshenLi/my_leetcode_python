
# 两分钟搞定 我已经不再是从前那个少年！！！！
# 和全排列一模一样

class Solution:
    def countArrangement(self, n: int) -> int:

        visited = [False] * (n + 1)
        self.res = 0

        def dfs(level):
            if level == n + 1:
                self.res += 1
                return None

            for i in range(1, n + 1):
                if visited[i] == False:
                    if i % level == 0 or level % i == 0:
                        visited[i] = True
                        dfs(level + 1)
                        visited[i] = False

        dfs(1)
        return self.res