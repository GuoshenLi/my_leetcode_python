import random
# # top_k 问题找对大的k个数字
# def sift(li, low, high):
#     i = low
#     tmp = li[i]
#     j = 2 * i + 1
#
#     while j <= high:
#         if j + 1 <= high and li[j + 1] < li[j]:
#             j = j + 1
#
#         if tmp > li[j]:
#             li[i] = li[j]
#             i = j
#             j = 2 * i + 1
#
#         else:
#             li[i] = tmp
#             break
#
#     else:
#         li[i] = tmp
#
#
#
# def topk(li, k):
#     heap = li[0: k]
#     # 建立堆
#     for i in range((k - 2) // 2, -1, -1):
#         sift(heap, i, k - 1)
#
#     # 维护这个堆为最大的k个数字
#     # 因为维护小根堆，所以堆顶最小
#     for i in range(k, len(li)):
#         if li[i] > heap[0]:
#             heap[0] = li[i]
#             sift(heap, 0, k - 1)
#
#     # 最终挨个出数
#     for i in range(k - 1, -1, -1):
#         heap[i], heap[0] = heap[0], heap[i]
#         sift(heap, 0, i - 1)
#
#     return heap



def sift(li, low, high):
    tmp = li[i]
    i = low
    j = 2 * i + 1

    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1

        if tmp > li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1

        else:
            li[i] = tmp
            break

    else:
        li[i] = tmp


def topk(li, k):
    heap = li[:k]    # index: 0, 1, ..., k - 1
    for i in range((k - 2) // 2, -1, -1):
        sift(li, 0, i)

    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(li, 0, k - 1)

    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(li, 0, i - 1)


    return heap

if __name__ == '__main__':
    li = [random.randint(0, 1000) for i in range(100)]
    print(topk(li, 100))

    li.sort(reverse=True)
    print(li[:100])