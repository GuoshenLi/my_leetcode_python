# 还是哈希表好用 不超时
class Solution:
    def maxProduct(self, words: List[str]) -> int:

        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                i_set = set(words[i])
                j_set = set(words[j])

                if not i_set & j_set:
                    res = max(res, len(words[i] * len(words[j])))

        return res

# 位运算 竟然超时
class Solution:
    def maxProduct(self, words: List[str]) -> int:

        # 26 个小写字母 可以用长度为26的位 去当作哈希表计算

        def no_common(word1, word2):
            bitmask1 = 0
            bitmask2 = 0

            for ch in word1:
                count = ord(ch) - ord('a')
                bitmask1 = bitmask1 | 1 << count

            for ch in word2:
                count = ord(ch) - ord('a')
                bitmask2 = bitmask2 | 1 << count

            return bitmask1 & bitmask2 == 0

        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if no_common(words[i], words[j]):
                    res = max(res, len(words[i]) * len(words[j]))

        return res


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n

        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                # add bit number bit_number in bitmask
                bitmask |= 1 << ord(ch) - ord('a')
            masks[i] = bitmask
            lens[i] = len(words[i])

        max_val = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    max_val = max(max_val, lens[i] * lens[j])
        return max_val
