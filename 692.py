from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        candidates = list(count.keys())
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]




class Word:
    def __init__(self, w, f):
        self.w = w
        self.f = f
    def __lt__(self, other):
        if self.f < other.f or (self.f == other.f and self.w > other.w):
                                                     # 字母排在越后的越小。
            return True
        else:
            return False

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = [Word(w, f) for w, f in collections.Counter(words).items()]
        heap = []
        for word in word_freq:
            if len(heap) >= k:
                if word.f > heap[0].f or (word.f == heap[0].f and word.w < heap[0].w):
                    # 判断要插进来，replace以后怎么调整（sift）就要看对象word的__lt__方法
                    heapq.heapreplace(heap, word)
            else:
                heapq.heappush(heap, word)

        ans = [""] * k
        for i in range(k - 1, -1, -1):
            ans[i] = heapq.heappop(heap).w
        return ans