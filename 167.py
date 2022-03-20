# O(nlogn) 二分查找加逐个搜索
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1

# 双指针 O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 双指针
        right = len(numbers) - 1
        left = 0

        while left < right:
            if numbers[right] + numbers[left] == target:
                return [left + 1, right + 1]
            elif numbers[right] + numbers[left] < target:
                left += 1
            else:
                right -= 1

