class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 画个图就可以了 nums[n] 其实要和 nums[n - 2] 去比较
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]

                else:
                    nums[i] = nums[i - 1]

                count += 1

        return count <= 1


