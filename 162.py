from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i - 1

        return len(nums) - 1
# 二分法 死背 迭代
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]: # 或者大于等于都可以
                right = mid
            else:
                left = mid + 1

        # 如果mid > mid + 1 很明显峰值在右边 所以right = mid
        # 如果mid < mid + 1 很明显峰值在左边 所以left = mid + 1

        return left

# 递归
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def helper(left, right):
            if left == right:
                return left

            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return helper(left, mid)
            else:
                return helper(mid + 1, right)

        return helper(0, len(nums) - 1)





def find2Dpeak(plane):
    """
    Finds a 2D peak in a 2D list of comparable types
    A 2D peak is an x in P such that it is greater than
    or equal to both its horizontal and both its
    vertical neighbors
    ex.
    [[1, 0, 0],
    [2, 2, 0],
    [0, 0, 0]]
    the top right corner is a peak
    the middle left and middle right elements are peaks
    the bottom right corner is a peak
    Complexity: 0(mlog(n))
    m行 n列
    代码是选中间那行 然后global max再最优 因此是 0(nlog(m))
    """
    m = len(plane)
    middle_row = plane[m // 2]
    middle_max = max(middle_row)
    j = middle_row.index(middle_max)
    
    if m == 1:
        return middle_max

    if middle_max < plane[m // 2 - 1][j]:
        return find2Dpeak(plane[:m // 2])
    elif middle_max < plane[m // 2 + 1][j]:
        return find2Dpeak(plane[m // 2 + 1:])
    else:
        return middle_max



if __name__ == "__main__":
    print(find2Dpeak([
        [1, 0, 0],
        [2, 2, 0],
        [0, 0, 0],
    ]))


