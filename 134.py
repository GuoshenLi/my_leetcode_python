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

        length = len(gas)
        i = 0
        while i < length:
            oilSum = 0
            index = i

            while oilSum + gas[index] - cost[index] >= 0:
                oilSum += (gas[index] - cost[index])
                index = (index + 1) % length

                if index == i:
                    return i
            i = index + 1
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




