import random


def bubble_sort(li):
    n = len(li)

    for i in range(n):
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


if __name__ == '__main__':

    li = [random.randint(1, 1000) for i in range(100)]

    bubble_sort(li)
    print(li)