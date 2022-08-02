class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while nums[i] != i:         # 发现这个坑里的萝卜不是自己家的
                temp = nums[i]          # 看看你是哪家的萝卜
                if nums[temp] == temp:  # 看看你家里有没有和你一样的萝卜
                    return temp         # 发现你家里有了和你一样的萝卜，那你就多余了，上交国家
                else:                   # 你家里那个萝卜和你不一样
                    nums[temp], nums[i] = nums[i], nums[temp]   # 把你送回你家去，然后把你家里的那个萝卜拿回来