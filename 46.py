class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        depth = len(nums)
        use = [True for _ in range(depth)]  # 若为True 则表明数字可以使用

        # 没有重复数字序列 不用跳过同层相同的 所以不用排序

        def dfs(tmp, use):

            if len(tmp) == depth:
                res.append(tmp[:])
                return None
            # 递归终止条件以后立刻写循环
            # i从0开始到最后这个循环的原因是因为数字能不能够要通过use数组来判断，不能简单地像组合数那道题目只能选一些index与             # index之后的数字
            for i in range(depth):
                if use[i] == False:
                    continue
                tmp.append(nums[i])
                use[i] = False
                dfs(tmp, use)
                tmp.pop()
                use[i] = True

        dfs([], use)
        return res