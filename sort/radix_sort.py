# 排序一般都是正整数
# 时间复杂度 O(kn) n 是数字个数 k 是最大数字的位数

from typing import *
def radix_sort(li):
    '''
    O(kn)
    :param li:
    :return:
    '''

    max_num = max(li)
    max_len = len(str(max_num))
    for i in range(max_len):
        # k次循环 O(k)
        buckets = [[] for _ in range(10)]
        for val in li:
            # O(n)
            digit = (val // 10 ** i) % 10 # 那一个位数算出来
            buckets[digit].append(val)


        li.clear()
        # O(n)
        for bucket in buckets:
            li.extend(bucket)

if __name__ == "__main__":
    import random
    max_number = 10000
    li = [random.randint(0, max_number) for i in range(1000)]
    radix_sort(li)
    print(li)