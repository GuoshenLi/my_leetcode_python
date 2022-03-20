# 先来一个暴力法 竟然能过
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = [digit for digit in str(num)]
        res = num
        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):

                num_list[i], num_list[j] = num_list[j], num_list[i]
                res = max(res, int(''.join(num_list)))
                num_list[j], num_list[i] = num_list[i], num_list[j]

        return res


class Solution:

    def maximumSwap(self, num: int) -> int:
        num_list = [int(digit) for digit in str(num)]
        loc = {}
        for i, j in enumerate(num_list):
            loc[j] = i

        for i in range(len(num_list)):
            for compare in range(9, num_list[i], -1):
                if compare in loc and loc[compare] > i:
                    num_list[i], num_list[loc[compare]] = num_list[loc[compare]], num_list[i]

                    return int(''.join(map(str, num_list)))

        return num


print(Solution().maximumSwap(num = 9973))