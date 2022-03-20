# 首位加0 可以免除判断边界条件 牛逼
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        tmp = [0]+flowerbed+[0]
        for i in range(1, len(tmp)-1):
            if tmp[i-1] == 0 and tmp[i] == 0 and tmp[i+1] == 0:
                tmp[i] = 1  # 在 i 处栽上花
                n -= 1   
        return n <= 0   # n 小于等于 0 ，表示可以栽完花

