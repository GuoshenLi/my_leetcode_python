# 与39一样 画搜索树
# 此题要注意去重

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(index, tmp):
            if sum(tmp) == target:
                res.append(tmp[:])
                return None
            if sum(tmp) > target:
                return None

            # index代表层

            for i in range(index, n):
                # 新的一层可选节点开始看有没有重复 所以i > index 若i > 0则有问题
                # 因为i不是从头开始选，而是从index开始选。
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                tmp.append(candidates[i])
                dfs(i + 1, tmp)
                tmp.pop()

        dfs(0, [])
        return res