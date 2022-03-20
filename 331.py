class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#': return True
        # 特判
        in_degree = out_degree = 0
        preorder = preorder.split(',')
        n = len(preorder)

        for i in range(n):
            if i == 0:
                if preorder[0] == '#':
                    return False
                # 特判
                out_degree += 2
                continue

            if preorder[i] == '#':
                in_degree += 1

            else:
                in_degree += 1
                out_degree += 2

            if i != n - 1 and in_degree >= out_degree: return False

        return in_degree == out_degree


