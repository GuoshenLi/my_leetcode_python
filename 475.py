# 暴力法 超时
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:


        houses.sort()
        heaters.sort()

        res = 0


        for house in houses:
            near = float('+inf')
            for heater in heaters:
                near = min(abs(house - heater), near)
            res = max(res, near)

        return res

# 通过
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()

        radius = 0
        i = 0
        # i = 0要写在外面，双指针和house 同时移动
        # 房屋左右侧的热水器，取距离小的那个，最终取的是所有房屋所需最大的那个半径。
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
            #  一直找到处于房屋右侧的热水器 等于也算右侧

            if i == 0:
                radius = max(radius, heaters[i] - house)

            elif i == len(heaters):
                radius = max(radius, house - heaters[-1])

            else:
                radius = max(radius, min(heaters[i] - house, house - heaters[i - 1]))

        return radius
