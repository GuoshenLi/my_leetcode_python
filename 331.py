class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')

        in_degree = 0
        out_degree = 0
        n = len(preorder)
        if preorder[0] == '#':
            return n == 1

        for i in range(n):
            if i == 0:
                out_degree += 2
            else:

                if preorder[i].isdigit():
                    in_degree += 1
                    out_degree += 2

                elif preorder[i] == '#':
                    in_degree += 1


                if i != n - 1 and in_degree >= out_degree:
                    return False


        return in_degree == out_degree
