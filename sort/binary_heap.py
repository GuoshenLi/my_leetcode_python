# 原来li[:-1] 是一个堆 新加了一个元素在最后 现在要把整个列表都变成堆
def sift_up(li):
    tmp = li[-1]
    n = len(li)
    i = n - 1  # 最后一个位置
    j = (i - 1) // 2 # parent

    while j >= 0:
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = (i - 1) // 2

        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp




def sift_down(li, low, high):
    tmp = li[low]
    i = low
    j = 2 * i + 1

    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j = j + 1

        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1

        else:
            li[i] = tmp
            break

    else:
        li[i] = tmp


li = [5,2,7,3,1,8,8]
heap = []
for i in range(len(li)):
    heap.append(li[i])
    sift_up(heap)


for i in range((len(li) - 2) // 2, -1, -1):
    sift_down(li, i, len(li) - 1)

print(heap)
print(li)