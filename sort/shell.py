# shell排序其实是分组的插入排序
import random

def insertion_sort(li, gap):
    n = len(li)
    for i in range(gap, n):
        tmp = li[i]
        j = i - gap
        while j >= 0 and tmp < li[j]:
            li[j + gap] = li[j]
            j -= gap

        li[j + gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insertion_sort(li, d)
        d = d // 2


li = [random.randint(0, 20) for i in range(20)]
shell_sort(li)
print(li)