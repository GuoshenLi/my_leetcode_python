# 暴力法
class Solution:
    def maxArea(self, height: List[int]) -> int:

        quantity = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                h = min(height[i], height[j])
                quantity = max(quantity, h * (j - i))

        return quantity

# 双指针法 可以证明！其正确性
class Solution:
    def maxArea(self, height: List[int]) -> int:
        quantity = 0
        left = 0
        right = len(height) - 1
        while left < right:
            quantity = max(quantity, (right - left) * min(height[left], height[right]))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return quantity