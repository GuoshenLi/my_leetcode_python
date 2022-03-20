# 暴力法 超时
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        def is_ugly(num):
            while num != 1:
                if num % 2 == 0:
                    num = num // 2
                elif num % 3 == 0:
                    num = num // 3
                elif num % 5 == 0:
                    num = num // 5
                else:
                    return False

            return True

        count = 0
        i = 1
        while True:
            if is_ugly(i):
                count += 1
                if count == n:
                    return i
            i += 1



# 字结跳动 三指针
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]



# 用堆更好想
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        heap = [1]
        visited = {1}
        for i in range(2, n + 1):
            num = heapq.heappop(heap)
            if num * 2 not in visited:
                heapq.heappush(heap, num * 2)
                visited.add(num * 2)
            if num * 3 not in visited:
                heapq.heappush(heap, num * 3)
                visited.add(num * 3)
            if num * 5 not in visited:
                heapq.heappush(heap, num * 5)
                visited.add(num * 5)

        return heapq.heappop(heap)

print(Solution().nthUglyNumber(n = 10))
