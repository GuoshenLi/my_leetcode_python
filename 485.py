class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #result为最后的最大值，count为目前最小值，index为当前索引
        result = count = 0
        #判断条件
        for index in range(len(nums)):
            #如果为1则直接count+1
            if nums[index] == 1:
                count += 1
            #如果为0则更新最大值
            else:
                result = max(result, count)
                count = 0

        #这里要考虑末尾一直为1的情况，返回result,max最大值
        return max(result, count)