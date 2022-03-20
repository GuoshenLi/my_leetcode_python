# 对列表进行排序 (一般排序都是整数) 已知列表中的数范围都在 0 ～ 100 之间 计数排序时间复杂度 O(n)

def count_sort(li, max_number = 100):
    count_array = [0 for _ in range(max_number + 1)] # 0 ~ 100
    for val in li:
        count_array[val] += 1

    li.clear()
    for index, val in enumerate(count_array):
        if val != 0:
            for i in range(val):
                li.append(index)

if __name__ == "__main__":
    import random
    max_number = 1000
    li = [random.randint(0, max_number) for i in range(1000)]
    count_sort(li, max_number)
    print(li)

