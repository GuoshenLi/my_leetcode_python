# 找不到规律就直接暴力 回溯

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # 找规律
        # 从 1 到 n - k

        res = list(range(1, n - k + 1))

        diff = k
        flag = 1

        for i in range(k):
            res.append(res[-1] + flag * diff)
            diff -= 1
            flag = -flag

        return res

