# 用队列 广度优先搜索
from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        queue = deque()
        queue.append((0,0))
        self.seen = set()
        while queue:
            remain_x, remain_y = queue.popleft()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in self.seen:
                continue
            self.seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            queue.append((x, remain_y))
            # 把 Y 壶灌满。
            queue.append((remain_x, y))
            # 把 X 壶倒空。
            queue.append((0, remain_y))
            # 把 Y 壶倒空。
            queue.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            queue.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            queue.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False

