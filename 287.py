from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        hash_table = set()

        for item in nums:
            if item in hash_table:
                return item
            else:
                hash_table.add(item)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        for i in range(len(nums)):

            index = abs(nums[i]) - 1
            if nums[index] < 0:
                return index + 1
            else:
                nums[index] = -nums[index]




class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                fast = 0
                while nums[slow] != nums[fast]:
                    fast = nums[fast]
                    slow = nums[slow]

                return nums[slow]

print(Solution().findDuplicate(nums = [1, 3, 4, 2, 2]))


# 更容易理解一点
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast, slow = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                fast = 0
                while fast != slow:
                    fast = nums[fast]
                    slow = nums[slow]

                return slow


print(Solution().findDuplicate(nums = [1, 3, 4, 2, 2]))