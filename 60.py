class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        visited = [False] * (n + 1)
        factorial = [1] * (n + 1)

        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        tmp = []

        def dfs(n, k, level):

            if level == n:
                return None

            cnt = factorial[n - 1 - level]

            for i in range(1, n + 1):
                if visited[i] == True:
                    continue

                if cnt < k:
                    k -= cnt
                    continue

                visited[i] = True
                tmp.append(i)
                dfs(n, k, level + 1)

                return None

        dfs(n, k, 0)
        return ''.join(map(str, tmp))



class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        visited = [False] * n
        self.res = ''
        self.step = 0
        def dfs(index, tmp):
            if index >= n:
                self.step += 1
                if self.step == k:
                    self.res = ''.join(map(str, tmp))
                    return True
                return False

            for i in range(n):
                if visited[i] == False:
                    visited[i] = True
                    tmp.append(i + 1)
                    if dfs(index + 1, tmp): return True
                    tmp.pop()
                    visited[i] = False

        dfs(0, [])
        return self.res
