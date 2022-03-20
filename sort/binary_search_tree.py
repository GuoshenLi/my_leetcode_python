class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BST:

    def __init__(self, val_list):
        self.root = None
        for i in val_list:
            self.root = self.add_node(self.root, i)


    def add_node(self, node, val):
        if not node: node = TreeNode(val)
        if node.val > val:
            node.left = self.add_node(node.left, val)
        elif node.val < val:
            node.right = self.add_node(node.right, val)
        return node


    def remove(self, node, val):
        if not node: return None
        if node.val < val:
            node.right = self.remove(node.right, val)
        elif node.val > val:
            node.left = self.remove(node.left, val)
        else: # 等于
            if not node.left: node = node.right
            elif not node.right: node = node.left
            else: # 左右都有子树
                cur = node.right
                while cur.left:
                    cur = cur.left
                node.val = cur.val
                node.right = self.remove(node.right, cur.val)

        return node

    def search(self, node, val):
        if not node:
            print('not in tree!')
            return None

        if node.val > val:
            self.search(node.left, val)
        elif node.val < val:
            self.search(node.right, val)
        else:
            print('found!')


    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)


bst = BST([1,2,3,4,5])
bst.inorder(bst.root)
bst.search(bst.root, 6)

bst.remove(bst.root, 5)
bst.inorder(bst.root)
bst.search(bst.root, 4)
