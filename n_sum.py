import random
from operator import length_hint

# n 数之和

nums = [2, 3, 1, 5, 1, 10, -3, 2]


# def get_three_sum(nums, target, res):
#     nums.sort()
#     n = len(nums)
#
#     for i in range(n):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#
#         left = i + 1
#         right = n - 1
#
#         while left < right:
#             if nums[i] + nums[left] + nums[right] == target:
#                 res.append([nums[i], nums[left], nums[right]])
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#                 left += 1
#                 right -= 1
#             elif nums[i] + nums[left] + nums[right] > target:
#                 right -= 1
#             else:
#                 left += 1
#
# res = []
# get_three_sum(nums, 8, res)
# print(res)

# 递归
nums = [1, 2, -3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def get_n_sum(n, left, right, target):
    res = []
    if n == 2:
        # 排序之后的2 sum

        while left < right:
            if nums[left] + nums[right] == target:
                res.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return res

    else:
        for i in range(left, len(nums)):
            if i > left and nums[i] == nums[i - 1]:
                continue

            tmp_list = get_n_sum(n - 1, i + 1, len(nums) - 1, target - nums[i])

            for sub_list in tmp_list:
                res.append([nums[i]] + sub_list)

        return res

nums.sort()
print(get_n_sum(6, 0, len(nums) - 1, 30))
