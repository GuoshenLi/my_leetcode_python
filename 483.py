class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        # k ^ 0 + k ^ 1 + ... + k ^ (m - 1) = n ===> (k ^ m - 1)/(k - 1) = n
        # 因为k >= 2 所以长度m小于等于二进制时的长度
        M = len(bin(n)) - 2
        # m > 2时 k ^ (m - 1) < n < (k + 1) ^ (m - 1) ===> k = int(n ^ {1 / (m - 1)})
        # m = 2时 一定是一个有效解, n = (n -1) ^ 1 + (n - 1) ^ 0
        # 因为对于任何一个数 如7654 肯定可以写成7653进制
        # 这样子长度为2 也可以写成11
        # 因为转换进制之后如果越长 进制数越小
        # 否则转换进制之后越短 进制数越大
        # 因此要进制数越小 就要从长度最长开始

        for m in range(M, 2, -1):
            k = int(pow(n, 1 / (m - 1)))
            # 验证这样得到的k是否真的让(k^m-1)/(k-1)=n成立
            if (pow(k, m) - 1) // (k - 1) == n and (pow(k, m) - 1)%(k - 1) ==0:
                return str(k)

        # 是在找不到 肯定有一个万能的解 就是n - 1进制
        return str(n - 1)
