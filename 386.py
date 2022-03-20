# 十叉树 前序遍历
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(num):
            if num > n:
                return None
            res.append(num)
            for i in range(10):
                dfs(10 * num + i)


        for i in range(1, 10):
            dfs(i)

        return res



class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(list(range(1, n + 1)), key=lambda x: str(x))


from functools import cmp_to_key
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def compare(x, y):
            x, y = str(x), str(y)
            if x < y:
                return -1
            elif x > y:
                return 1
            else:
                return 0

        return sorted([i for i in range(1, n + 1)], key = cmp_to_key(compare))



