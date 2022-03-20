class Solution:
    # 对每一个点用一个哈希表 记录到这个点的距离分别有多少个点 然后再排列组合
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            hashmap = collections.defaultdict(int)
            for j in range(len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dis = dx * dx + dy * dy
                hashmap[dis] += 1
            for val in hashmap.values():
                res += val * (val - 1)
        return res


