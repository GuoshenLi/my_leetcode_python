class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        #从开根号值开始向1值靠近，这样第一个满足area % w == 0的值就是所求列表
        w = int(math.sqrt(area))
        while w >= 1:
            if area % w == 0:
                return [area // w, w]
            w -= 1