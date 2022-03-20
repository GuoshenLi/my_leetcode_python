# 统计所有大写字母出现的次数
class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        length = len(word)
        upper_sum = 0
        for char in word:
            if char.isupper():
                upper_sum += 1

        if upper_sum == length:
            return True

        if upper_sum == 0:
            return True

        if upper_sum == 1 and word[0].isupper():
            return True

        return False


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.title():
            return True

        flag = 'Upper' if word[0].isupper() else 'Lower'

        for char in word[1:]:
            if char.isupper() and flag != 'Upper':
                return False
            elif char.islower() and flag != 'Lower':
                return False

        return True



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper()==word or word.lower()==word or word.title()==word

