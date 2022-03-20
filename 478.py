from random import random
# 拒绝采样
# 只要生成(-1, 1) 圆心在原点，半径为1的随机数，然后平移和缩放即可
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:

        while True:
            rand_x = 2 * random() - 1
            rand_y = 2 * random() - 1
            if rand_x ** 2 + rand_y ** 2 <= 1:
                return [rand_x * self.radius + self.x_center, rand_y * self.radius + self.y_center]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()