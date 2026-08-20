from typing import List
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

class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        '''
            左 右 根
            左边比它小
            右边比它大
        '''

        if not postorder: return True
        root = postorder[-1]

        i = len(postorder) - 2

        while i >= 0 and postorder[i] > root:
            i -= 1

        j = i

        while j >= 0:
            if postorder[j] > root:
                return False
            j -= 1

        left = True
        right = True
        if i > 1:
            left = self.verifyTreeOrder(postorder[0: i + 1])
        if i < len(postorder) - 1:
            right = self.verifyTreeOrder(postorder[i + 1: -1])

        return left and right

print(Solution().verifyTreeOrder([4,6,5,9,8]))