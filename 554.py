from typing import List
# 算法思想的确牛逼!!!!
# 就是所有层数 - 间隙最多的数量 就是穿过最少的 牛逼
from collections import defaultdict


class Solution:

    def leastBricks(self, wall: List[List[int]]) -> int:
        # 特判一下 如果长度都为1 则要穿过全部
        if all(len(row) == 1 for row in wall):
            return len(wall)

        middle_count = defaultdict(int)

        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                middle_count[pos] += 1

        return len(wall) - max(middle_count.values())


Solution().leastBricks(wall=[[1,2,2,1],
      [3,1,2],
      [1,3,2],
      [2,4],
      [3,1,2],
      [1,3,1,1]])