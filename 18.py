from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4: return []
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                left = j + 1
                right = n - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return res


print(Solution().fourSum([1,0,-1,0,-2,2], target = 0))


# nSum 递归
class Solution:
    def nSum(self, nums: List[int], n:int, target: int) -> List[List[int]]:
        nums.sort()
        return self.getNSum(nums, n, 0, target)


    def getNSum(self, nums, n, start, target):
        length = len(nums)
        curList = []
        if n == 2:
            left, right = start, length - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    curList.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        elif n > 2:
            for i in range(start, length):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subList = self.getNSum(nums, n - 1, i + 1, target - nums[i])
                # [[1,0,0], [0, 0, 1]]
                for list in subList:
                    curList.append(list + [nums[i]])
        return curList



print(Solution().nSum(nums=[1,2,3,4,5,6,7], n=5, target=15))