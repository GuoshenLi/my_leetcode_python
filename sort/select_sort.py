import random


def insertion_sort(li):
    n = len(li)
    for i in range(n):
        k = i # 最小值的下标为k
        for j in range(i + 1, n):
            if li[j] < li[k]:
                k = j
        li[k], li[i] = li[i], li[k]


li = [random.randint(0, 100) for _ in range(100)]
insertion_sort(li)
print(li)


