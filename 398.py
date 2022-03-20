from random import choice
import numpy as np

from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.table = defaultdict(list)
        for i in range(len(nums)):
            self.table[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.table[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)







# 蓄水池抽样
# 假设当前正要读取第n个数据，则我们以1/n的概率留下该数据，否则以(n-1)/n 的概率留下前n-1个数据中的一个。
# 而前n-1个数组留下的那个概率为1/(n-1), 因此最终留下上次n-1个数中留下的那个数的概率为[1/(n-1)]*[(n-1)/n] = 1/n,
# 符合均匀分布的要求

# 数据动态供给也可以等概率

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = 0
        ans = None

        for i in range(len(self.nums)):
            if self.nums[i] == target:
                cnt += 1
                if random.randint(1, cnt) == cnt:
                    ans = i


        return ans

