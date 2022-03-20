# 暴力解法
class Solution:

    def maxRotateFunction(self, A: List[int]) -> int:
        if not A: return 0
        len_A = len(A)
        max_ = float('-inf')
        tmp = [0 for _ in range(len_A)]
        for k in range(len_A):
            sum_ = 0
            for i in range(len_A):
                index = (i + k) % len_A
                tmp[index] = A[i]
                sum_ += index * tmp[index]

            max_ = max(max_, sum_)
        return max_


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        # 写出递推公式
        # F(1) = F(0) + Sum(A) - nA[n - 1]
        # F(2) = F(1) + Sum(A) - nA[n - 2]

        # F(3) = F(2) + Sum(A) - nA[n - 3]
        # F(4) = F(3) + Sum(A) - nA[n - 4]
        # ...
        # F(n - 1) = F(n - 2) + Sum(A) - nA[0]

        if not A: return 0
        sum_A = sum(A)
        n = len(A)

        F_now = 0
        for i in range(n):
            F_now += i * A[i]
        max_ = F_now

        for i in range(1, n):
            F_next = F_now + sum_A - n * A[n - i]
            max_ = max(max_, F_next)
            F_now = F_next

        return max_




