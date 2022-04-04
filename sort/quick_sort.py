# import random
#
#
# def partition(nums, left, right):
#     temp = nums[left]
#
#     while left < right:
#         while left < right and nums[right] >= temp:
#             right -= 1
#
#         nums[left] = nums[right]
#
#         while left < right and nums[left] <= temp:
#             left += 1
#
#         nums[right] = nums[left]
#
#     nums[left] = temp
#     return left
#
#
# def quick_sort(nums, left, right):
#     if left < right:
#         mid = partition(nums, left, right)
#         quick_sort(nums, left, mid - 1)
#         quick_sort(nums, mid + 1, right)
#
#
# if __name__ == "__main__":
#     nums = [random.randint(0, 100) for i in range(100)]
#     quick_sort(nums, 0, len(nums) - 1)
#     print(nums)
#
#
#
#
# # if __name__ == '__main__':
# #     li = [random.randint(1, 100) for _ in range(100)]
# #
# #     quick_sort(li, 0, len(li) - 1)
# #     print(li)



# 非递归 non-recursive
def partition(a, start, end):

    # Pick the rightmost element as a pivot from the list
    pivot = a[end]

    # elements less than the pivot will go to the left of `pIndex`
    # elements more than the pivot will go to the right of `pIndex`
    # equal elements can go either way
    pIndex = start

    # each time we find an element less than or equal to the pivot,
    # `pIndex` is incremented, and that element would be placed
    # before the pivot.
    for i in range(start, end):
        if a[i] <= pivot:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex = pIndex + 1

    # swap `pIndex` with pivot
    a[pIndex], a[end] = a[end], a[pIndex]

    # return `pIndex` (index of the pivot element)
    return pIndex


# Iterative Quicksort routine
def iterativeQuicksort(a):

    # create a stack for storing sublist start and end index
    stack = []

    # get the starting and ending index of a given list
    start = 0
    end = len(nums) - 1

    # push the start and end index of the array into the stack
    stack.append((start, end))

    # loop till stack is empty
    while stack:

        # remove top pair from the list and get sublist starting
        # and ending indices
        start, end = stack.pop()

        # rearrange elements across pivot
        pivot = partition(nums, start, end)

        # push sublist indices containing elements that are
        # less than the current pivot to stack
        if pivot - 1 > start:
            stack.append((start, pivot - 1))

        # push sublist indices containing elements that are
        # more than the current pivot to stack
        if pivot + 1 < end:
            stack.append((pivot + 1, end))


# Iterative Implementation of Quicksort
if __name__ == '__main__':

    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]

    iterativeQuicksort(a)

    # print the sorted list
    print(a)