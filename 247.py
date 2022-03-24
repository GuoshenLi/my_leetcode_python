class Solution:
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
