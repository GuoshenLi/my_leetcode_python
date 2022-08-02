class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack = []
        cur_max = float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > cur_max: return False
            while stack and postorder[i] < stack[-1]:
                cur_max = stack.pop()

            stack.append(postorder[i])

        return True


class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


