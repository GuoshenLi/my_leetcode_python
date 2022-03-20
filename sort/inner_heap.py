import heapq # 优先队列
import random



li = list(range(100))
random.shuffle(li)

print(li)

heapq.heapify(li) # 建立堆
print(li)
for i in range(10):

    print(heapq.heappop(li))
