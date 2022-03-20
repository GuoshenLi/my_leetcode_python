# 以 0 和 end 作为比较对象（定死）
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        ######## 就是这两句 #######
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()
        ##########################

        length = len(nums)
        left, right = 0, length - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[0] <= nums[mid]:  # mid在左半边有序数组
                if nums[0] <= target < nums[mid]:  # 并且目标在左半边有序数组中
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # mid在右半边有序数组
                if nums[mid] < target <= nums[-1]:  # 并且目标在右半边有序数组中
                    left = mid + 1
                else:
                    right = mid - 1

        return False



# 以left 和 right 作为比较对象（活动）
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        length = len(nums)
        left, right = 0, length - 1

        while left <= right:
            # 去重
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:  # mid在左半边有序数组
                if nums[left] <= target < nums[mid]:  # 并且目标在左半边有序数组中
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # mid在右半边有序数组
                if nums[mid] < target <= nums[right]:  # 并且目标在右半边有序数组中
                    left = mid + 1
                else:
                    right = mid - 1

        return False