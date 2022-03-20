# 百度测试一面 很简单！！！

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        tmp = []
        tmp.append(self.dist(p1, p2))
        tmp.append(self.dist(p1, p3))
        tmp.append(self.dist(p1, p4))
        tmp.append(self.dist(p2, p3))
        tmp.append(self.dist(p2, p4))
        tmp.append(self.dist(p3, p4))

        tmp.sort()
        # 正方形肯定四条边相等并且对角线相等 否则就是菱形（对角线不等） 而且要判断边长不为0
        return tmp[0] != 0 and tmp[0] == tmp[1] == tmp[2] == tmp[3] and tmp[4] == tmp[5]

    def dist(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2



