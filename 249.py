from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # 字符串之间可以移位得到必然是每一位距离差对应一致的时候
        def hashCounter(string):
            return tuple(((ord(string[i]) - ord(string[i-1])) % 26) for i in range(1 , len(string))) if len(string) > 1 else 0

        ans = defaultdict(list)
        for s in strings:
            ans[hashCounter(s)].append(s)
        return list(ans.values())
