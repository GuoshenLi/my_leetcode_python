# 二分查找
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 如果找到nums[mid] == target 的话，则
# 在此之前不可能存在target的结束，所以搜索开始的位置要另right = mid(要在前面搜索，包括mid的位置)
# 在此之后不可能存在target的开始，所以搜索结束的位置另left = mid(要在后面搜索，包括mid的位置)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0:
            return [-1, -1]

        first_position = self.__find_first_position(nums, size, target)
        if first_position == -1:
            return [-1, -1]
        last_position = self.__find_last_position(nums, size, target)
        return [first_position, last_position]

    def __find_first_position(self, nums, size, target):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # nums[mid] == target
                right = mid

        if nums[left] == target:
            return left
        else:
            return -1

    def __find_last_position(self, nums, size, target):
        left = 0
        right = size - 1
        while left < right:
            # 试看数组 [5, 7, 7, 8, 8, 8, 10]
            # 判断最后一个数字一定要 +1， 否则会死循环
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                # nums[mid] == target
                left = mid

        # 由于能走到这里，说明在数组中一定找得到目标元素，因此这里不用再做一次判断
        return left





class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums: return res
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target: return res

        res[0] = left

        left = 0
        right = n - 1

        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        res[1] = left

        return res
