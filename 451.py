from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        res = ''
        count_s = Counter(s)
        count_s = count_s.most_common()

        for item in count_s:
            res += item[0] * item[1]


        return res


# 其实没必要 都是nlogn
import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        items = [(-val, key) for key, val in count.items()]
        # 大根堆 加负号
        heapq.heapify(items)
        res = ""
        while heap:
            val, key = heapq.heappop(items)
            res += key * (-val)
        return res

