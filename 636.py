from typing import List
# 636 画图 遇到end要+1 并且要维护pre指针指向前一个时间节点

# 这道题关键是单线程非抢占cpu，就是说父函数调用子函数，子函数结束之后、父函数才有可能结束。
# 不会出现父函数结束了，子函数继续运行的情况。

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res, stack, pre = [0] * n, [], None
        for log in logs:
            i, op, ti = log.split(':')
            i, ti = int(i), int(ti)
            if op == 'start':
                if stack:
                    res[stack[-1]] += ti - pre
                stack.append(i)
            else:
                ti += 1
                res[stack.pop()] += ti - pre
            pre = ti
        return res


Solution().exclusiveTime(n = 2, logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])