class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> List[int]:

        stack = [root]
        res = []
        while stack:
            tmp = stack.pop()
            if isinstance(tmp, TreeNode):
                stack.append(tmp.right)
                stack.append(tmp.left)
                stack.append(tmp.val)

            elif isinstance(tmp, int):
                res.append(tmp)
            else:
                continue

        return res