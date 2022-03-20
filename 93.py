from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == len(s):
                            n1 = int(s[:a])
                            n2 = int(s[a:a+b])
                            n3 = int(s[a+b:a+b+c])
                            n4 = int(s[a+b+c:a+b+c+d])
                            if n1 < 256 and n2 < 256 and n3 < 256 and n4 < 256:
                                ip = '.'.join(map(str, [n1, n2, n3, n4]))
                                if len(ip) == len(s) + 3:
                                    # n1, n2, n3, n4 不能有0开始的数字 "+3" 是因为3个.(点)连起来
                                    res.append(ip)
        return res



class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        n = len(s)

        def dfs(tmp, start):
            if len(tmp) == 4:
                if start == n:
                    final = '.'.join(map(str, tmp))
                    if len(final) == n + 3:
                        res.append(final)
                return None

            for i in range(3):
                if start + i + 1 > n:
                    break
                tmp_num = int(s[start: start + i + 1])
                if 0 <= tmp_num <= 255:
                    tmp.append(tmp_num)
                    dfs(tmp, start + i + 1)
                    tmp.pop()

        dfs([], 0)

        return res


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        n = len(s)

        def dfs(tmp, start):
            if len(tmp) == 4:
                if start == n:
                    final = '.'.join(map(str, tmp))
                    # if len(final) == n + 3: # 去除前导0
                    res.append(final)
                return None

            for i in range(3):
                if start + i + 1 > n:
                    break
                tmp_num = s[start: start + i + 1]
                # 现在这里判断一下不会超时
                # 在这里判断有没有前导0。
                if len(tmp_num) == len(str(int(tmp_num))) and 0 <= int(tmp_num) <= 255:
                        tmp.append(int(tmp_num))
                        dfs(tmp, start + i + 1)
                        tmp.pop()

        dfs([], 0)

        return res






print(Solution().restoreIpAddresses('0000'))