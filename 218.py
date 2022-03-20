# https://leetcode-cn.com/problems/the-skyline-problem/solution/fen-er-zhi-zhi-er-fen-fa-dui-by-powcai/
class Solution:
    def getSkyline(self, buildings):
        if not buildings: return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)

    # 两个合并
    def merge(self, left, right):
        # 记录产生当前候选点的上一个左右建筑物的高度
        lheight = rheight = 0
        # 位置
        l = r = 0
        # 输出结果
        res = []
        while l < len(left) and r < len(right):
            if left[l][0] < right[r][0]:
                # current point
                cp = [left[l][0], max(left[l][1], rheight)] # 产生完候选点

                lheight = left[l][1] # 立刻更新一下lhright(上一个左边的点)
                l += 1
            elif left[l][0] > right[r][0]:
                cp = [right[r][0], max(right[r][1], lheight)]
                rheight = right[r][1]
                r += 1
            # 相等情况
            else:
                cp = [left[l][0], max(left[l][1], right[r][1])]
                lheight = left[l][1]
                rheight = right[r][1]
                l += 1
                r += 1
            # 和前面高度比较，不一样才加入
            if len(res) == 0 or res[-1][1] != cp[1]:
                res.append(cp)


        # 有点归并排序那味了
        while l < len(left):
            res.append(left[l])
            l += 1

        while r < len(right):
            res.append(right[r])
            r += 1

        return res
