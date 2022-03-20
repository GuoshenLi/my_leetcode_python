import random

# def merge(nums, low, mid, high):
#     left = low
#     right = mid + 1
#     tmp = []
#     while left <= mid and right <= high:
#         if nums[left] <= nums[right]:
#             tmp.append(nums[left])
#             left += 1
#         else:
#             tmp.append(nums[right])
#             right += 1
#
#     while left <= mid:
#         tmp.append(nums[left])
#         left += 1
#     while right <= high:
#         tmp.append(nums[right])
#         right += 1
#     nums[low: high + 1] = tmp
#
# def merge_sort(nums, left, right):
#     if left < right:
#         mid = (left + right) // 2
#         merge_sort(nums, left, mid)
#         merge_sort(nums, mid + 1, right)
#         merge(nums, left, mid, right)
#
#
#
# li = [random.randint(0, 20) for _ in range(20)]
# merge_sort(li, 0, len(li) - 1)
# print(li)
#
#
#



def merge(nums, left, mid, right):
    p1 = left
    p2 = mid + 1
    res = []

    while p1 <= mid and p2 <= right:
        if nums[p1] < nums[p2]:
            res.append(nums[p1])
            p1 += 1
        else:
            res.append(nums[p2])
            p2 += 1

    while p1 <= mid:
        res.append(nums[p1])
        p1 += 1

    while p2 <= right:
        res.append(nums[p2])
        p2 += 1


    nums[left: right + 1] = res


def merge_sort(nums, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)
        merge(nums, left, mid, right)




li = [random.randint(0, 20) for _ in range(20)]
merge_sort(li, 0, len(li) - 1)
print(li)

