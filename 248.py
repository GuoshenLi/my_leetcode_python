# 暴力解法竟然能过。
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:


        res = []
        for i in range(len(low), len(high) + 1):
            res.extend(self.findStrobogrammatic(i))


        return len(list(filter(lambda x: int(low) <= int(x) <= int(high), res)))

    def findStrobogrammatic(self, n: int) -> List[str]:

        def dfs(m):
            if not m:
                return ['']
            elif m == 1:
                return ['0', '1', '8']
            new_list = []
            for ans in dfs(m - 2):
                if n != m:
                    new_list.append('0' + ans + '0')
                new_list.append('6' + ans + '9')
                new_list.append('9' + ans + '6')
                new_list.append('1' + ans + '1')
                new_list.append('8' + ans + '8')
            return new_list

        return dfs(n)