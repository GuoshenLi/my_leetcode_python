# 数学方法
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        elif x == 0:
            return True

        mem = x
        # x > 0
        nums = 0
        while x > 0:
            digit = x % 10
            nums = nums * 10 + digit
            x = x // 10

        return mem == nums

# 字符串方法
class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True


