class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            count = 0
            for j in range(32):
                count += i & 1
                i = i >> 1
            res.append(count)

        return res

# 找规律
# 若n为奇数 则其1的个数比前面那个偶数 也就是n-1 多1个
# 若n为偶数 则其1的个数与n//2的那个偶数 的1的个数相同


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0 for i in range(num + 1)]

        for i in range(1, num + 1):
            if i % 2 == 1:  # 奇数
                res[i] = res[i - 1] + 1
            else:
                res[i] = res[i // 2]

        return res

