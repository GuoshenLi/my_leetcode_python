import random
import copy
# 原来li[:-1] 是一个堆 新加了一个元素在最后 现在要把整个列表都变成堆
def sift_up(li, low, high):
    tmp = li[high]
    i = high  # 最后一个位置
    j = (i - 1) // 2 # parent

    while j >= low:
        if tmp > li[j]:
            li[i] = li[j]
            i = j
            j = (i - 1) // 2

        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp



# sift_down 向下调整

def sift_down(li, low, high):
    '''

    :param li:
    :param low:
    :param high:
    :return:


    这个函数为调整函数，针对跟节点不满足堆的性质而跟节点的左右子树都满足堆的性质
    '''
    i = low
    tmp = li[i]
    j = 2 * i + 1 # 左子节点

    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j = j + 1 # j指向更大的子节点

        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1

        else:
            li[i] = tmp # 放到非叶子节点上
            break

    else:
        li[i] = tmp # 放到叶子节点上


def heap_sort_1(li):
    n = len(li)

    for i in range(n):
        sift_up(li, 0, i)

    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift_down(li, 0, i - 1) # 因为换完以后要更新最后一个元素为i - 1


def heap_sort_2(li):
    n = len(li)
    for i in range(((n - 2) // 2), -1, -1): #i表示调整部分的根的下标
        sift_down(li, i, n - 1)

    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift_down(li, 0, i - 1) # 因为换完以后要更新最后一个元素为i - 1


# 堆排序也很简单
if __name__ == "__main__":
    li = [random.randint(0, 100) for _ in range(1000)]
    li1 = copy.deepcopy(li)
    li2 = copy.deepcopy(li)
    heap_sort_1(li1)
    heap_sort_2(li2)
    print(li1)
    print(li2)

