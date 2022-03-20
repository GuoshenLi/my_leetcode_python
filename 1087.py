class Solution:
    def expand(self, s: str) -> List[str]:
        # [['a', 'b'], ['c'], ['d', 'e'], ['f']]
        # 用dfs


        candidates = []
        i = 0
        while i < len(s):
            tmp = []
            if s[i] == '{':
                i += 1
                while s[i] != '}':
                    if s[i].isalpha():
                        tmp.append(s[i])
                    i += 1
                i += 1

            else:
                tmp.append(s[i])
                i += 1

            candidates.append(tmp)

        # [['a', 'b'], ['c'], ['d', 'e'], ['f']]


        n = len(candidates)
        res = []

        def dfs(index, tmp):
            if index == n:
                res.append("".join(tmp[:]))
                return None

            for char in candidates[index]:
                tmp.append(char)
                dfs(index + 1, tmp)
                tmp.pop()


        dfs(0, [])
        return sorted(res)
