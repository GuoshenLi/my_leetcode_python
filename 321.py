# 跟402 移除k个数字一样，更难一点而已
class Solution:
    def maxNumber(self, nums1, nums2, k):

        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]


        # 比较当前元素大小，选择大的元素；
        # 如果一样大，比较后续元素；
        # 如此往复； python的代码非常简洁 注意利用[]list的大小比较关系 若[6, 7, 4]和[6, 7]比较，则前者大
        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger.pop(0))
            return ans

        return max(merge(pick_max(nums1, i), pick_max(nums2, k - i)) for i in range(k + 1) if
                   i <= len(nums1) and k - i <= len(nums2))

print(Solution().maxNumber(nums1 = [6,7], nums2 = [6,0,4], k = 5))



