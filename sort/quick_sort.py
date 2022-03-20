import random


def partition(nums, left, right):
    temp = nums[left]

    while left < right:
        while left < right and nums[right] >= temp:
            right -= 1

        nums[left] = nums[right]

        while left < right and nums[left] <= temp:
            left += 1

        nums[right] = nums[left]

    nums[left] = temp
    return left


def quick_sort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)


if __name__ == "__main__":
    nums = [random.randint(0, 100) for i in range(100)]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)

















# if __name__ == '__main__':
#     li = [random.randint(1, 100) for _ in range(100)]
#
#     quick_sort(li, 0, len(li) - 1)
#     print(li)
