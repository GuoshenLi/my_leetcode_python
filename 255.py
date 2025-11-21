class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:

        stack = []
        new_min = float('-inf')  # 初始化下限值
        n = len(preorder)

        for i in range(len(preorder)):
            if preorder[i] < new_min: return False
            while stack and preorder[i] > stack[-1]:
                new_min = stack.pop()
            stack.append(preorder[i])

        return True




class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if not preorder:
            return True

        root = preorder[0]
        i = 1

        while i < len(preorder) and preorder[i] < root:
            i += 1

        j = i
        while j < len(preorder):
            if preorder[j] < root:
                return False
            j += 1

        left = True
        if i > 1:
            left = self.verifyPreorder(preorder[1: i])

        right = True
        if i < len(preorder) - 1:
            right  =self.verifyPreorder(preorder[i: ])

        return left and right