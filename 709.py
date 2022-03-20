class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

# 最原始的写法 判断ascii码
class Solution:
    def toLowerCase(self, str: str) -> str:
        string = list(str)
        for i in range(len(string)):
            if ord(string[i]) >= ord('A') and ord(string[i]) <= ord('Z'):
                string[i] = chr(ord(string[i]) + 32)

        return ''.join(string)