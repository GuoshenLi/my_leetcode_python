import random, bisect
random.random()
class Solution:
    def __init__(self, rects):
        # 思路与528题类似，每个矩形包含的点数即为其权重。计算每个矩阵的权重。
        self.pre_sum = [0] * (len(rects) + 1)
        # 点数 = (x2 - x1 + 1) * (y2 - y1 + 1)， 需要加1，例如x1=1, x2=5,一共有5个点（5-1+1）

        for i in range(1, len(rects) + 1):
            self.pre_sum[i] = self.pre_sum[i - 1] + (rects[i - 1][2] - rects[i - 1][0] + 1) * (rects[i - 1][3] - rects[i - 1][1] + 1)
        self.rects = rects


    def pick(self):
        # random.randint(1, self.w[-1])：随机抽样
        # 在其中二分查找，确认应插入的位置。_left：当含有相等元素时，插在其左侧
        i = bisect.bisect_left(self.pre_sum, random.randint(1, self.pre_sum[-1]))
        # 在选中的矩形中随机选择坐标位置
        # 也可以不再使用random库，直接利用i计算出整个矩阵组中的第i个点的位置
        xi = random.randint(self.rects[i - 1][0], self.rects[i - 1][2])
        yi = random.randint(self.rects[i - 1][1], self.rects[i - 1][3])
        return [xi, yi]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

