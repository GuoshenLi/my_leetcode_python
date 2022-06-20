class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        pointers = [1 for i in range(len(primes))]

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):

            temp = min(dp[pointers[k]] * primes[k] for k in range(len(primes)))
            dp[i] = temp
            for k in range(len(primes)):
                if temp == dp[pointers[k]] * primes[k]:
                    pointers[k] += 1

        return dp[-1]