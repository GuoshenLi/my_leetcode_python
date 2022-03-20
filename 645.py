class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        S = sum(set(nums))
        return [sum(nums)-S ,len(nums)*(len(nums)+1)//2-S]


from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        count_num = Counter(nums)

        for i in range(1, len(nums) + 1):
            if i not in count_num:
                missing = i
            if count_num[i] > 1:
                repeat = i

        return [repeat, missing]

