class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 类似LC31. 我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。
        # 我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。

        # 1. 从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序. 如果这样的元素对不存在，则返回-1.
        # 2. 在 [j,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」.
        # 3. 将 A[i] 与 A[k] 交换. 可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序.

        s = list(str(n))
        n = len(s)
        i = n - 2

        while i >= 0:
            if s[i] < s[i + 1]:
                break
            # 从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
            i -= 1

        if i < 0:
            # 不存在这样的32位整数，则返回-1。
            return -1

        for j in range(n - 1, i, -1):
            # 在 [j,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」. 这里的j和k不需要相同（当然有可能相同）。
            if s[j] > s[i]:
                # 将 A[i] 与 A[k] 交换
                s[i], s[j] = s[j], s[i]
                break


        # 可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
        s[i + 1:] = s[i + 1:][::-1]
        res = int(''.join(s))
        if res > 2 ** 31 - 1: return -1
        return res






