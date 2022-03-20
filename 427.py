"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):1
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        return self.dfs(grid, 0, len(grid[0]) - 1, 0, len(grid) - 1)


    def dfs(self, grid, left, right, up, down):
        if self.is_same(grid, left, right, up, down):
            # 如果全部一样
            new_node = Node(val = grid[up][left], isLeaf = True)
            return new_node

        new_node = Node(val = grid[up][left], isLeaf = False)
        new_node.topLeft = self.dfs(grid, left, (left + right) // 2, up, (up + down) // 2)
        new_node.topRight = self.dfs(grid, (left + right) // 2 + 1, right, up, (up + down) // 2)
        new_node.bottomLeft = self.dfs(grid, left, (left + right) // 2, (up + down) // 2 + 1, down)
        new_node.bottomRight = self.dfs(grid, (left + right) // 2 + 1, right, (up + down) // 2 + 1, down)

        return new_node

    def is_same(self, grid, left, right, up, down):

        element = grid[up][left]
        for i in range(up, down + 1):
            for j in range(left, right + 1):
                if element != grid[i][j]:
                    return False

        return True





