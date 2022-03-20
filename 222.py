# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0

        return self.countNodes(root.left) + self.countNodes(root.right) + 1






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 首先需要明确完全二叉树的定义：它是一棵空树或者它的叶子节点只出在最后两层，若最后一层不满则叶子节点只在最左侧。
#
# 再来回顾一下满二叉的节点个数怎么计算，如果满二叉树的层数为h，则总节点数为：2^h - 1.
# 那么我们来对 root 节点的左右子树进行高度统计，分别记为 left 和 right，有以下两种结果：


# left == right。这说明，左子树一定是满二叉树，因为节点已经填充到右子树了，左子树必定已经填满了。
# 所以左子树的节点总数我们可以直接得到，是 2^left - 1，加上当前这个 root 节点，则正好是 2^left。再对右子树进行递归统计。
# left != right。说明此时最后一层不满，但倒数第二层已经满了，可以直接得到右子树的节点个数。
# 同理，右子树节点 +root 节点，总数为 2^right。再对左子树进行递归查找。



class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def count_depth(root):
            depth = 0
            while root:
                depth += 1
                root = root.left
            return depth

        # 求节点数目
        def count_node(root):
            if not root:
                return 0

            left_depth = count_depth(root.left)
            right_depth = count_depth(root.right)

            if left_depth == right_depth:
                return (1 << left_depth) + count_node(root.right)
            else:
                return (1 << right_depth) + count_node(root.left)

        return count_node(root)


