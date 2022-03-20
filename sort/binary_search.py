# 最基本
def binary_search(li, target):

    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2

        if li[mid] == target:
            return True
        elif li[mid] > target:
            right = mid - 1
        elif li[mid] < target:
            left = mid + 1

    return False


# 三分查找
def ternary_search(li, target, left, right):
    if right >= left:
        midl = left + (right - left) // 3
        midr = right - (right - left) // 3

        if li[midl] == target:
            return midl
        if li[midr] == target:
            return midr
        if target < li[midl]:
            return ternary_search(li, target, left, midl - 1)
        elif target > li[midr]:
            return ternary_search(li, target, midr + 1, right)
        else:
            return ternary_search(li, target, midl + 1, midr - 1)

    return -1

li = [2,2,2,3,4,5,6,7, 10, 10]
print(ternary_search(li, 10, 0, len(li) - 1))

# # 四个派生 找第一个小于等于，找第一大于等于，找最后一个小于等于，找最后一个大于等于
#
#
# # 找最后一个大于等于target的数字
# def the_first_bi(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         mid = (left + right + 1) // 2
#         if nums[mid] > target:
#             right = mid - 1
#         else:
#             left = mid
#     return left
#
#
#
#
# # 找第一个大于等于target的数字
# def the_first_bi(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#     return left
#
#
#
# # 找最后一个小于等于target的数字
# def the_first_bi(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left < right:
#         mid = (left + right + 1) // 2
#         if nums[mid] > target:
#             right = mid - 1
#
#         else:
#             left = mid
#     return left
#
# # print(the_first_bi(nums = [1,1,2,2,3,4,5,6,7], target = 2.5))
#
#
#
# # 找第一个小于等于
# def the_first_bi(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#
#     return left

