import random



def insertion_sort(li):
    # 插入排序有一个变量叫做last sorted
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1 # j 就是last sorted的index
        while j >= 0 and tmp < li[j]:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = tmp



li = [random.randint(0, 100) for _ in range(100)]
insertion_sort(li)
print(li)




