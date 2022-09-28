import heapq
import random
# 小根堆

def sift_down(li, low, high):


    i = low
    tmp = li[i]
    j = 2 * i + 1

    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1

        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1

        else:
            li[i] = tmp
            break

    else:
        li[i] = tmp


def sift_up(li, low, high):

    tmp = li[high]
    i = high
    j = (i - 1) // 2

    while j >= low:
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = (i - 1) // 2
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp



def heapify(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift_down(li, i, n - 1)


def heappop(li):
    li[0], li[-1] = li[-1], li[0]
    res = li.pop()
    if not li: return res

    sift_down(li, 0, len(li) - 1)
    return res


def heappush(li, val):

    li.append(val)
    sift_up(li, 0, len(li) - 1)



# li = [random.randint(0, 100) for _ in range(10)]
# heapify(li)
# print(li)


li = []
for i in [random.randint(0, 100) for _ in range(10)]:
    heappush(li, i)
print(li)
# test_ commit
