# 暴力法 超时
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            single = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                single *= nums[j]

            res.append(single)
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [0 for i in range(n)]
        post_prod = [0 for i in range(n)]
        # 前后缀数组存储的是在当前下标前面或者后面的元素的乘积

        pre_prod[0] = 1
        post_prod[n - 1] = 1

        for i in range(1, n):
            pre_prod[i] = pre_prod[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            post_prod[i] = post_prod[i + 1] * nums[i + 1]

        res = []
        for i in range(n):
            res.append(pre_prod[i] * post_prod[i])

        return res

# 常数空间复杂度
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [0 for _ in range(len(nums))]
        pre = 1

        for i in range(len(nums)):
            ans[i] = pre
            pre = pre * nums[i]

        r = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= r
            r *= nums[i]

        return ans


