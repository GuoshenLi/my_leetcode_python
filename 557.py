class Solution(object):
    def reverseWords(self, s):

        s = s.split(' ')
        return ' '.join(item[::-1] for item in s)





class Solution(object):
    def reverseWords(self, s):
        n = len(s)
        left = 0
        right = n - 1

        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        i, j = left, left
        res = ''

        while j <= right:
            while j <= right and s[j] != ' ':
                j += 1

            for k in range(j - 1, i - 1, -1):
                res += s[k]


            while j <= right and s[j] == ' ':
                j += 1
                res += ' '
            i = j

        return res


print(Solution().reverseWords(s = "Let's take LeetCode contest"))