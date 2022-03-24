class WordDistance:

    def __init__(self, words: List[str]):
        from collections import defaultdict
        self.words_loc = defaultdict(list)
        for idx, val in enumerate(words):
            self.words_loc[val].append(idx)


    def shortest(self, word1: str, word2: str) -> int:
        res = float("inf")
        for a in self.words_loc[word1]:
            for b in self.words_loc[word2]:
                res = min(res, abs(a-b))
        return res