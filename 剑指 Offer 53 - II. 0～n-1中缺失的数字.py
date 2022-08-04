class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right= n - 1
        '''
            注意一个点 如果 nums[mid] != mid
            证明错误的位置 只能在mid这个位置及之前发生
            
            如果nums[mid] == mid
            则错误的位置只能在mid之后发生
            
            仔细品味
        '''

        while left < right:
            mid = (left + right) // 2
            if nums[mid] != mid:
                right = mid
            else:
                left = mid + 1



        return left + 1 if nums[left] == left and left == n - 1 else left