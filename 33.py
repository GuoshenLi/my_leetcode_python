# 以 0 和 end 作为比较对象（定死）
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 一定要小于等于
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            return -1

# 以right和left作为比较对象（活动）
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
            [0,1,2,4,5,6,7]

            [4,5,6,7,0,1,2]

        '''

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2
            if nums[mid] == target: return mid
            # 一定要小于等于
            # 因为要看左边有序还是右边有序，就算等于也是左边有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


