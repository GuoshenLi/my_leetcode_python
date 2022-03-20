
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        queue = ['']
        phone = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno', '7':'pqrs','8':'tuv','9':'wxyz'}
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[digit]:
                    queue.append(tmp + letter)
        return queue

# 回溯
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(tmp, index):
            if index == len(digits):
                res.append(''.join(tmp))
                return None

            for char in phoneMap[digits[index]]:
                tmp.append(char)
                dfs(tmp, index + 1)
                tmp.pop()

        dfs([], 0)

        return res

