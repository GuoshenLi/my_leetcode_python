class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        if len(s) < k:
            return s[::-1]

        start = 0
        res = ''
        while start < len(s):

            tmp = s[start: start + 2 * k]
            if len(tmp) <= k:
                res += tmp[::-1]
                break

            elif k < len(tmp) < 2 * k:
                res += tmp[:k][::-1]
                res += tmp[k:]
                break

            else:  # length == 2k

                res += tmp[:k][::-1]
                res += tmp[k:]

                start += 2 * k

        return res


print(Solution().reverseStr(s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", k = 39))