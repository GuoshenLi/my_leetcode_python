# 穷举
class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        length = len(gas)
        i = 0
        for i in range(length):
            oilSum = 0
            index = i

            while oilSum + gas[index] - cost[index] >= 0:
                oilSum += (gas[index] - cost[index])
                index = (index + 1) % length

                if index == i:
                    return i

        return -1



class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start = 0
        n = len(gas)

        while start < n:
            tmp = 0 # 当前油数
            count = 0
            i = start
            while count < n:
                tmp += (gas[i] - cost[i])
                if tmp < 0:
                    start = start + count + 1
                    break
                count += 1
                i = (i + 1) % n

            else:
                return start

        return -1





class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        '''总油量 < 总耗油量，一定无解'''
        if sum(gas) < sum(cost):
            return -1

        '''sum(gas) >= sum(cost)，一定有解【题目保证唯一解】'''
        n = len(gas)
        start = 0       # 记录出发点，从索引0开始
        total = 0       # 记录汽车实际油量
        for i in range(n):
            total += gas[i] - cost[i]  # 每个站点加油量相当于 gas[i] - cost[i]
            if total < 0:       # 在i处的油量<0，说明从之前站点出发的车均无法到达i
                start = i+1     # 尝试从下一个站点i+1重新出发
                total = 0       # 重新出发时油量置为0

        return start    # 解是唯一的
