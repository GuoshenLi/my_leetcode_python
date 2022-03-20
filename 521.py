# 暴力法 超时 只通过7个

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        hash_map = {}
        length_a = len(a)
        length_b = len(b)

        def dfs_a(start, tmp):

            if ''.join(tmp) in hash_map:
                hash_map[''.join(tmp)] += 1
            else:
                hash_map[''.join(tmp)] = 1

            for end in range(start, length_a):
                tmp.append(a[end])
                dfs_a(end + 1, tmp)
                tmp.pop()

        dfs_a(0, [])

        def dfs_b(start, tmp):

            if ''.join(tmp) in hash_map:
                hash_map[''.join(tmp)] += 1
            else:
                hash_map[''.join(tmp)] = 1

            for end in range(start, length_b):
                tmp.append(b[end])
                dfs_b(end + 1, tmp)
                tmp.pop()

        dfs_b(0, [])

        max_len = -1

        for k, v in hash_map.items():
            if v == 1:
                max_len = max(max_len, len(k))

        return max_len

# 其实很简单 只要举例子三种情况即可
# 若 a 与 b 一样 则没有特殊的子序列
# 若 a != b 且len(a) == len(b) 则最长特殊子序列就是a 或 b
# 若 a != b 且len(a) != len(b) 则最长特殊子序列就是长度更长的哪个序列

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        else:
            return max(len(a), len(b))