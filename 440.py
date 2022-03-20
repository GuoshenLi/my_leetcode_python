# 暴力
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        li = [str(i) for i in range(1, n)]

        li.sort()
        return int(li[k - 1])



import heapq
# 超时
class Node:
    def __init__(self, val):
        self.val = str(val)

    def __lt__(self, n1):
        # 大根堆 写大于号即可
        if self.val > n1.val:
            return True
        else:
            return False

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        heap = []
        for i in range(1, k + 1):
            heapq.heappush(heap, Node(i))

        for i in range(k + 1, n + 1):
            if heap[0].val > str(i):
                heapq.heapreplace(heap, Node(i))

        return int(heap[0].val)




class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        self.res = None
        self.step = 0
        def dfs(num):
            if num > n:
                return None
            if self.step == k:
                self.res = num
                return None

            if num == 0:
                for next_ in range(1, 10):
                    if next_ <= n:
                        self.step += 1
                        dfs(next_)

            else:
                for next_ in range(10 * num, 10 * num + 10):
                    if next_ <= n:
                        self.step += 1
                        dfs(next_)


        dfs(0)
        return self.res



# 其实就相当于10叉树 前序遍历k个元素
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def num_node(cur):
            next = cur + 1
            count = 0
            while cur <= n:
                # 因为是完全十叉树
                # 如果这一层是满的 则 个数为next - cur
                # 因此只可能有最后一层没有填满
                # 没有填满的那一层的个数就是 n + 1 - cur
                # cur 其实就是这一层的开头
                # 因此要取一个min
                count += min(next - cur, n + 1 - cur)
                next *= 10
                cur *= 10

            return count

        # cur == 1 已经走1步了 因此global_step = 1
        cur = 1
        global_step = 1

        while global_step < k:
            steps = num_node(cur)    # cur为跟节点的树有多少个结点

            if steps + global_step <= k:
                # 只能往右走
                global_step += steps # 为什么可以直接加step? 要仔细体会
                                     # 以cur为跟节点的树有step个结点 因此在当前cur下
                                     # 遍历完要cur下面的结点要cur - 1步, 还要多1步去右边的结点
                cur += 1
            else:

                # 很明显在以cur为跟节点的树当中
                # 我就前序遍历往下走一步
                # 因此cur * 10 且 global_step += 1

                global_step += 1
                cur *= 10

        return cur

Solution().findKthNumber(n = 123, k = 10)
# k == 10 证明按照前序遍历 走10步