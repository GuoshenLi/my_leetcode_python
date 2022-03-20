class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        memo = {}

        def dfs(s1, s2):

            if (s1, s2) in memo:
                return memo[(s1, s2)]

            N = len(s1)
            if N == 0: return True
            if N == 1: return s1 == s2


            for i in range(1, N):
                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    memo[(s2, s1)] = True
                    return True
                elif dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i]):
                    memo[(s1, s2)] = True
                    memo[(s2, s1)] = True
                    return True

            memo[(s1, s2)] = False
            memo[(s2, s1)] = False
            return False


        flag = dfs(s1, s2)
        print(memo)
        return flag