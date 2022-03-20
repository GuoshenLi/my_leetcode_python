# 和leetcode 127 一样类型的题目
#
from typing import List
from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        bank = set(bank)
        if end not in bank:
            return -1

        if start in bank:
            bank.remove(start)

        queue = deque()
        queue.append([start, 0])

        while queue:
            gene, step = queue.popleft()

            if gene == end:
                return step

            for i in range(8):
                for j in ['A', 'G', 'C', 'T']:
                    new_gene = gene[:i] + j + gene[i + 1:]
                    if new_gene in bank:
                        queue.append([new_gene, step + 1])
                        bank.remove(new_gene)

        return -1

Solution().minMutation(start =  "AACCGGTT", end =    "AACCGGTA", bank =  ["AACCGGTA"])