# 暴力回溯 穷举 竟然可以通过
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        hash_map = {}

        def dfs(start, tmp, string, length):

            if ''.join(tmp) in hash_map:
                hash_map[''.join(tmp)] += 1
            else:
                hash_map[''.join(tmp)] = 1

            for end in range(start, length):
                tmp.append(string[end])
                dfs(end + 1, tmp, string, length)
                tmp.pop()

        for string in strs:
            dfs(0, [], string, len(string))

        max_len = -1

        for k, v in hash_map.items():
            if v == 1:
                max_len = max(max_len, len(k))

        return max_len

# 一个一个排查
# 与上一个题目做对比
# 如果存在这样的特殊序列，那么它一定是某个给定的字符串。
# 检查每个字符串是否是其他字符串的子序列。如果不是，则它是一个特殊序列。
# 最后返回长度最大的特殊序列。如果不存在特殊序列，返回 -1。
# 最长特殊子序列 = 最长子序列(就是其本身)+该序列不能是其他序列的子序列
# 这个题目的确有点智障



class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def is_subsequent(x, y):
            i = j = 0

            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    i += 1
                    j += 1
                else:
                    j += 1

            return i == len(x)


        res = -1
        for i in range(len(strs)):
            for j in range(len(strs)):

                if i == j:
                    continue

                if is_subsequent(strs[i], strs[j]):
                    break
            else:

                res = max(res, len(strs[i]))

        return res


