# 先凑第一个k 再凑第二个k，再凑第三个k
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        target = total_sum // k
        if total_sum % k != 0: return False
        nums = sorted(nums, reverse=True)
        if nums[0] > target: return False

        n = len(nums)
        vis = [False] * n

        def backtrack(k, tmp):
            if k == 1:
                return True

            if tmp == target:
                return backtrack(k - 1, 0)

            for i in range(n):
                if vis[i] == False and tmp + nums[i] <= target:

                    vis[i] = True
                    tmp += nums[i]
                    if backtrack(k, tmp):
                        return True
                    tmp -= nums[i]
                    vis[i] = False

            return False

        return backtrack(k, 0)


# 和473做法一样
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        target = total_sum // k
        if total_sum % k != 0: return False
        nums = sorted(nums, reverse=True)

        tmp = [0] * k
        n = len(nums)

        def dfs(index):
            if index == n: return all(i == target for i in tmp)


            for i in range(k):
                if tmp[i] + nums[index] <= target:
                    tmp[i] += nums[index]
                    if dfs(index + 1): return True
                    tmp[i] -= nums[index]

            return False

        return dfs(0)

