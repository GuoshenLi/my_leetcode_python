# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 初始化，最小值赋值为无穷大，last_value记录上一个节点的值
        self.min_value, self.last_value = float("inf"), -1
        self.mid_order(root)
        return self.min_value

    def pengding_num(self, val):

        # 第一个节点赋值给last_value
        if self.last_value == -1:
            self.last_value = val
        else:
            # 每次求差的绝对值的最小值，更新
            self.min_value = min(self.min_value, abs(val - self.last_value))
            self.last_value = val

    # 中序遍历
    def mid_order(self, root):

        if root:
            self.mid_order(root.left)
            # 处理当前节点
            self.pengding_num(root.val)
            self.mid_order(root.right)


# 迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        pre = -1
        min_ = float('+inf')
        stack = [root]
        while stack:
            stuff = stack.pop()
            if isinstance(stuff, TreeNode):
                stack.append(stuff.right)
                stack.append(stuff.val)
                stack.append(stuff.left)

            elif isinstance(stuff, int):
                if pre == -1:
                    pre = stuff
                else:
                    min_ = min(min_, abs(stuff - pre))
                    pre = stuff

        return min_

