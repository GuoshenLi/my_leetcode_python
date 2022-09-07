from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        each_length = len(words[0])
        total_length = len(words) * each_length
        words = Counter(words)
        res = []
        for i in range(len(s)):
            slice_ = s[i: i + total_length]
            if len(slice_) < total_length: break
            count_this_peace = Counter()
            for j in range(0, total_length, each_length):
                count_this_peace[slice_[j: j + each_length]] += 1
            if count_this_peace == words:
                res.append(i)

        return res



# O(len(s) * len(words[0])
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        num_words, each_length, length_s = len(words), len(words[0]), len(s)
        for i in range(each_length):
            if i + num_words * each_length > length_s:
                break

            differ = Counter()
            for start in range(i, i + num_words * each_length, each_length):
                word = s[start: start + each_length]
                differ[word] += 1

            for word in words:
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]

            if len(differ) == 0:
                res.append(i)

            for start in range(i + each_length, length_s, each_length):
                if start + num_words * each_length > length_s: break
                word = s[start + (num_words - 1) * each_length: start + num_words * each_length]
                differ[word] += 1
                if differ[word] == 0:
                    del differ[word]
                word = s[start - each_length: start]
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]

                if len(differ) == 0:
                    res.append(start)

        return res




#  判断的时候没有优化
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        each_length = len(words[0])
        num_words = len(words)
        total_length = each_length * num_words
        length_s = len(s)
        words = Counter(words)

        for i in range(each_length):

            # 从i位置开始做滑动窗口
            if i + total_length > length_s:
                break
            count = Counter()
            for start in range(i, i + total_length, each_length):
                count[s[start: start + each_length]] += 1

            if count == words:
                res.append(i)

            for start in range(i + total_length, length_s, each_length):
                if start + each_length > length_s: break
                count[s[start: start + each_length]] += 1
                count[s[start - total_length: start - total_length + each_length]] -= 1
                if count[s[start - total_length: start - total_length + each_length]] == 0:
                    del count[s[start - total_length: start - total_length + each_length]]

                if count == words:
                    res.append(start - total_length + each_length)

        return res


print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))