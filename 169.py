class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        memo = {}
        for item in nums:
            memo[item] = memo.get(item, 0) + 1
            if memo[item] > len(nums) // 2:
                return item


# 摩尔投票法 多数投票法
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # major是候选人
        # count是这个候选人的票数（抵消后）
        #

        major = None
        count = 0

        for n in nums:
            if count == 0:
                major = n
                count = 1
            elif n == major:
                count = count + 1
            else:
                count = count - 1

        return major



# 摩尔投票法 多数投票法
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # major是候选人
        # count是这个候选人的票数（抵消后）
        #

        major = None
        count = 0

        for n in nums:
            if major == n:
                count += 1
            elif count == 0:
                major = n
                count += 1
            else:
                count -= 1

        return major