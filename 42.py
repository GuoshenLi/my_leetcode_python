# 单调栈

class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                cur = stack.pop()
                if not stack:
                    break
                # 当前height[i]与pop以后的栈顶height[stack[-1]]能形成多大的积水
                # stack不能为空，若为空，则形不成低洼。
                ans += (min(height[i], height[stack[-1]]) - height[cur]) * (i - stack[-1] - 1)
            stack.append(i)

        return ans






# 暴力法 python超时
# 每一根柱子上面究竟可以积累多少雨水

class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0
        for i in range(1, len(height) - 1):
            max_left, max_right = 0, 0
            # 寻找 max_left
            for j in range(0, i):
                max_left = max(max_left, height[j])
            # 寻找 max_right
            for j in range(i + 1, len(height)):
                max_right = max(max_right, height[j])

            if min(max_left, max_right) > height[i]:
                ans += min(max_left, max_right) - height[i]

        return ans




# 优化的暴力解法 动态规划
# pre_compute the max

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n - 1):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])

        for i in range(n - 2, 0, -1):
            rightMax[i] = max(rightMax[i + 1], height[i + 1])

        ans = 0
        for i in range(1, n - 1):
            if min(leftMax[i], rightMax[i]) - height[i] > 0:
                ans += min(leftMax[i], rightMax[i]) - height[i]

        return ans

# 最优解法
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans

