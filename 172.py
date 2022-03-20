# 会超时 但是简单
class Solution():
    def trailingZeroes(self, n: int) -> int:

        # Calculate n!
        n_factorial = 1
        for i in range(2, n + 1):
            n_factorial *= i

        # Count how many 0's are on the end.
        zero_count = 0
        while n_factorial % 10 == 0:
            zero_count += 1
            n_factorial //= 10

        return zero_count

# 简单方法！背诵！
class Solution():
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # 循环减半是log2(n) 循环除以5 是log5（n） 也是log（n）
        while n > 0:
            count += n // 5
            n = n // 5

        return count



