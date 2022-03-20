def bucket_sort(li, n = 100, max_num = 10000):
    buckets = [[] for _ in range(n)]
    for val in li:
        i = min(val // (max_num // n), n - 1)
        # 防止最大的数字进来 要放到最后一个桶里 否则会越界
        buckets[i].append(val)
        # [0, 2, 4, 3] # 冒泡一次 解决有序的问题
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j - 1]
            else:
                break

    li.clear()
    for bucket in buckets:
        li.extend(bucket)


if __name__ == "__main__":
    import random
    max_number = 10000
    li = [random.randint(0, max_number) for i in range(1000)]
    bucket_sort(li, n = 100, max_num = max_number)
    print(li)