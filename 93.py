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




# 我已经不再是从前那个少年
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:


        n = len(s)
        res = []


        def dfs(start, tmp):
            if start == n:
                if len(tmp) == 4:
                    res.append('.'.join(tmp))
                return None

            for end in range(start, min(start + 3, n)):
                slice_ = s[start: end + 1]
                if start != end and slice_[0] == '0':
                    continue
                if 0 <= int(slice_) <= 255:
                    tmp.append(slice_)
                    dfs(end + 1, tmp)
                    tmp.pop()

        dfs(0, [])
        return res







print(Solution().restoreIpAddresses('0000'))