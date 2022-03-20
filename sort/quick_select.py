import random
def partition(li, left, right):
    tmp = li[left]

    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1

        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1

        li[right] = li[left]

    li[left] = tmp

    return left



if __name__ == "__main__":
    # 找下标是 len(li) - k 的数字
    # top_k

    li = [random.randint(0, 20) for _ in range(15)]
    n = len(li)
    k = 10
    target = n - k
    left, right = 0, n - 1
    while True:
        mid = partition(left, right)
        if mid == target:
            print(li[mid])
            break

        elif mid < target:
            left = mid + 1

        else:
            right = mid - 1

