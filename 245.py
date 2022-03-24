class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            # 双指针
            first = -1
            second = -1
            min_dis = float('+inf')
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    if first == -1:
                        first = i
                    else:
                        second = first
                        first = i
                        min_dis = min(min_dis, first - second)

        else:
            first = -1
            second = -1
            min_dis = float('+inf')

            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    first = i
                elif wordsDict[i] == word2:
                    second = i

                if first != -1 and second != -1:

                    min_dis = min(min_dis, abs(first - second))


        return min_dis


