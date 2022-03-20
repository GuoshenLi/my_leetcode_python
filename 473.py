# 这个方法在这里不超时
class Solution:
    def makesquare(self, nums: List[int]) -> bool:

        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums: return False
        if sum(nums) % 4 != 0: return False
        pre_side = sum(nums) // 4
        length = len(nums)
        tmp = [0, 0, 0, 0]
        # 排序
        nums.sort(reverse=True)

        def dfs(index):
            if index == length:
                return tmp[0] == tmp[1] == tmp[2] == tmp[3] == pre_side

            for i in range(4):
                # 剪掉
                if tmp[i] + nums[index] <= pre_side:
                    tmp[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    tmp[i] -= nums[index]

            return False

        return dfs(0)


# 一个一个凑 和698 一摸一样！ 但是反而超时
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks: return False
        if sum(matchsticks) % 4 != 0: return False
        per_side = sum(matchsticks) // 4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        if matchsticks[0] > per_side: return False
        visited = [False] * n

        def dfs(k, tmp):
            if k == 1: return True
            if tmp == per_side: return dfs(k - 1, 0)

            for i in range(n):
                if visited[i] == False and tmp + matchsticks[i] <= per_side:
                    tmp += matchsticks[i]
                    visited[i] = True
                    if dfs(k, tmp): return True
                    tmp -= matchsticks[i]
                    visited[i] = False

            return False

        return dfs(4, 0)