# 死背 寻找最小值 left < right 即可 唯一一个不用等于号的
# 肯定有 所以说不用等号 最终返回nums[left]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1          # 左闭右闭区间，如果用右开区间则不方便判断右值
        while left < right:                     # 循环不变式，如果left == right，则循环结束
            mid = (left + right) // 2           # 地板除，mid更靠近left
            if nums[mid] > nums[right]:         # 中值 > 右值，最小值在右半边，收缩左边界
                left = mid + 1                  # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            elif nums[mid] < nums[right]:       # 明确中值 < 右值，最小值在左半边，收缩右边界
                right = mid                     # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处
        return nums[left]                       # 循环结束，left == right，最小值输出nums[left]或nums[right]均可


# 最新
class Solution:
    # 肯定有最小值
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # 因为递增的数组 翻一部分过来 最小值肯定在右边有序数组中
        # 所以跟右边去比
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            # 严格小于 很明显只能right = mid
            else:
                left = mid + 1
            # 若大于 right 很明显left = mid + 1
            # 若等于 right 也要 left = mid + 1 因为最小值肯定也在右边
            # 这个逻辑是对的 自己仔细体会

        return nums[left]
