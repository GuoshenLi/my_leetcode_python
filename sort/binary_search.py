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


def binary_search_recur(nums, target, left, right):
    if right >= left:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search_recur(li, target, mid + 1, right)
        else:
            return binary_search_recur(li, target, left, mid - 1)

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
# 找第一个大于等于target的数字   找最后一个小于等于target的数字

