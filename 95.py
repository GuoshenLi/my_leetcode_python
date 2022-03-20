class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        return self.dfs(1, n)

    def dfs(self, start, end):
        # 从start 到 end开始构造 构造出来的树的root的集合
        # 其中跟节点为start到end
        if start > end: return [None]
        res = []

        for i in range(start, end + 1):

            left_list = self.dfs(start, i - 1)
            right_list = self.dfs(i + 1, end)

            for left in left_list:
                for right in right_list:
                    cur_node = TreeNode(i)
                    cur_node.left = left
                    cur_node.right = right

                    res.append(cur_node)

        return res