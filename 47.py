# 回溯难
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        depth = len(nums)
        use = [True for _ in range(depth)]

        def dfs(tmp, use):
            if len(tmp) == depth:
                res.append(tmp[:])
                return None

            for i in range(depth):
                if use[i] == False:
                    continue
                # 判断条件 use[i - 1] == True 一定要这样！
                # 同一层去重 单独写if i > 0 and nums[i] == nums[i - 1]: 绝对有问题
                # 再怎么说也要 i > index and ... 那一层可以选择的分支有没有重复 而不是重头开始判断
                # 但是下面这行use[i - 1] == True 仍然很难理解 == False 也对
                # use[i - 1] == True 判断i - 1在当前路径构造当中有没有被占用，如果没有被占用，则跳过（在同一层）
                # 若被占用，则在（不同层）可以继续构造 需要仔细体会 举例11‘2 仔细体会
                if i > 0 and nums[i] == nums[i - 1] and use[i - 1] == True:
                    continue

                tmp.append(nums[i])
                use[i] = False
                dfs(tmp, use)
                tmp.pop()
                use[i] = True

        dfs([], use)
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False for i in range(n)]
        table = set()
        def dfs(tmp):
            if len(tmp) == n:
                if tuple(tmp) not in table:
                    table.add(tuple(tmp))
                return None

            for i in range(n):
                if visited[i] == True:
                    continue

                visited[i] = True
                tmp.append(nums[i])
                dfs(tmp)
                visited[i] = False
                tmp.pop()

        dfs([])

        return list(table)

