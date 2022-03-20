class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 其实就是上次的进阶版本
        # k指针

        nums = [1]
        k = len(primes)
        i_index = [0] * k # k指针在这里了

        for i in range(1, n):
            ugly = min([primes[j] * nums[i_index[j]] for j in range(k)])
            nums.append(ugly)
            for j in range(k):
                if ugly == primes[j] * nums[i_index[j]]:
                    i_index[j] += 1

        return nums[n - 1]

