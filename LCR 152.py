class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        if not postorder: return True
        root = postorder[-1]
        i = 0
        # 找到第一个大于根的元素的位置
        while i < len(postorder) - 1 and postorder[i] < root:
            i += 1
        # 检查左侧部分是否都小于根节点
        j = i
        while j < len(postorder) - 1:
            if postorder[j] < root:
                return False
            j += 1
        # 递归检查左右子树
        left = True
        if i > 0:
            left = self.verifyTreeOrder(postorder[:i])

        right = True

        if i < len(postorder) - 1:
            right = self.verifyTreeOrder(postorder[i:-1])

        return left and right