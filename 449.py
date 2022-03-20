# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 二叉搜索树 值唯一 才可以这样做
# 因为有一个操作是.index 因此如果值不唯一 .index 就默认最前面那一个 就会出错！！！
# 所以直接被 那个前序遍历 和前序遍历恢复即可

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.pre_o = []
        self.pre_order(root)
        return ','.join(self.pre_o)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        pre_o = list(map(int, data.split(',')))
        in_o = sorted(pre_o)
        return self.build(pre_o, in_o)

    def pre_order(self, root):

        if root:
            self.pre_o.append(str(root.val))
            self.pre_order(root.left)
            self.pre_order(root.right)

    def build(self, pre_o, in_o):
        if not pre_o and not in_o:
            return None
        val = pre_o[0]
        mid = in_o.index(val)
        root = TreeNode(val)

        root.left = self.build(pre_o[1: mid + 1], in_o[: mid])
        root.right = self.build(pre_o[mid + 1:], in_o[mid + 1:])

        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return 'None'

        return str(root.val) + ' ' + self.serialize(root.left) + ' ' + self.serialize(root.right)


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        def buildtree(li):
            val = li.pop(0)
            if val == 'None': return None
            root = TreeNode(val)
            root.left = buildtree(li)
            root.right = buildtree(li)

            return root

        li = data.split()
        return buildtree(li)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans