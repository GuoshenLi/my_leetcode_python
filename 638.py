# 记忆化递归 个人觉得这个也不是回溯
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(needs)
        memo = {}
        def dfs(needs):
            if str(needs) in memo: return memo[str(needs)]

            money = sum(needs[i] * price[i] for i in range(n))

            for spe in special:
                temp = needs[:]
                if all(needs[i] >= spe[i] for i in range(n)):
                    for i in range(n):
                        temp[i] -= spe[i]
                    money = min(money, spe[n] + dfs(temp))

            memo[str(needs)] = money
            return memo[str(needs)]

        return dfs(needs)

