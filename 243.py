class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:

        p1 = -1
        p2 = -1
        res = float("inf")
        for idx, word in enumerate(words):
            if word == word1 : p1 = idx
            if word == word2 : p2 = idx

            if (p1 != -1 and p2 != -1): res = min(res, abs(p1 - p2))

        return res



from collections import defaultdict
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:


        '''
            table = {
                'practice':[0],
                'makes':[1, 4],
                'perfect':[2],
                'coding':[3],
            }


        '''
        table = defaultdict(list)
        for i in range(len(words)):
            table[words[i]].append(i)

        return min(abs(idx1 - idx2) for idx1 in table[word1] for idx2 in table[word2])



    