class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        # 排列组合

        if n == 0:
            return 1

        n = min(n , 10)

        ans = 10
        base = 9
        sum = 9
        for i in range(1, n):
            sum = sum * base
            ans = ans + sum
            base = base - 1

        return ans


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:


        visited = [False] * 10 # 0 ~ 9

        self.res = 0
        def dfs(level):
            self.res += 1
            if level == n:
                return None

            if level == 0:
                for i in range(1, 10):
                    if visited[i] == True:
                        continue
                    visited[i] = True
                    dfs(level + 1)
                    visited[i] = False

            else:
                for i in range(10):
                    if visited[i] == True:
                        continue
                    visited[i] = True
                    dfs(level + 1)
                    visited[i] = False



        dfs(0)
        return self.res


print(Solution().countNumbersWithUniqueDigits(n = 2))
