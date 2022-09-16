from typing import List, Tuple

def MaxMin1(arr: List[int]) -> Tuple[int, int]:
    Max, Min = arr[0], arr[0]
    # 2 * (n - 1) 次比较
    for i in range(1,len(arr)):
        if arr[i] < Min:
            Min = arr[i]
        if arr[i] > Max:
            Max = arr[i]
    return Max,Min



def MaxMin2(arr: List[int]) -> Tuple[int, int]:
    n = len(arr)
    # 若数组个数为偶数，则比较前两个元素，较大的作为当前最大值，较小的作为当前最小值
    # 若数组个数为奇数，则让第一个元素作为当前最大值和最小值
    # 总的比较次数为3[n/2] 每一个数对要比较3次
    p = 1
    Max, Min = arr[0], arr[0]
    if n % 2 == 0:
        p = 2
        if arr[0] > arr[1]:
            Min = arr[1]
        else:
            Max = arr[1]

    # 剩下的元素成对比较
    while p < n - 1:
        if arr[p] < arr[p + 1]:
            if arr[p + 1] > Max:
                Max = arr[p + 1]
            if arr[p] < Min:
                Min = arr[p]
        else:
            if arr[p] > Max:
                Max = arr[p]
            if arr[p + 1] < Min:
                Min = arr[p + 1]
        p += 2

    return Max, Min
