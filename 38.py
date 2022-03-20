# dfs + 双指针
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'

        res = ''
        tmp = self.countAndSay(n - 1)
        # if tmp == '1211':
        # 双指针
        left = right = 0
        while right < len(tmp):
            if tmp[right] != tmp[left]:
                res += str(right - left) + tmp[left]
                left = right

            right += 1

        res += str(right - left) + tmp[left]
        return res

