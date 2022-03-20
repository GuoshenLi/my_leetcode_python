class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:

            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                # 如果当前low和high指的不一样
                # 那就左边跳一个或者右边跳一个
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True

