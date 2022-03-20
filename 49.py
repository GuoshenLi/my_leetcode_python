from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1

            table[tuple(count)].append(string)

        return list(table.values())



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str_ in strs:
            # sorted(str) 之后会变成list 所以要join

            index_str = ''.join(sorted(str_))
            if index_str in res.keys():
                res[index_str].append(str_)
            else:
                res[index_str] = [str_]

        return list(res.values())

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        # 利用defaultdict
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())
