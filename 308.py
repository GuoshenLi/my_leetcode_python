class SegTree:  # 线段树--数组实现
    def __init__(self, n: int):
        self.tree = [0 for _ in range(4 * n)]
        self.n = n

    def update(self, idx: int, val: int) -> None:
        self._update(0, 0, self.n - 1, idx, val)

    def query(self, query_left: int, query_right: int) -> int:
        return self._query(0, 0, self.n - 1, query_left, query_right)

    def _update(self, node: int, start: int, end: int, idx: int, val: int) -> None:
        if start == end:
            self.tree[node] = val
            return None
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        mid = (start + end) // 2
        if idx <= mid:
            self._update(left_node, start, mid, idx, val)
        else:
            self._update(right_node, mid + 1, end, idx, val)
        self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def _query(self, node: int, start: int, end: int, query_left: int, query_right: int) -> int:
        if query_right < start or query_left > end: return 0
        elif query_left <= start and query_right >= end: return self.tree[node]
        elif start == end: return self.tree[node]
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        mid = (start + end) // 2

        left_sum = self._query(left_node, start, mid, query_left, query_right)
        right_sum = self._query(right_node, mid + 1, end, query_left, query_right)
        return left_sum + right_sum

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.Row, self.Col = len(matrix), len(matrix[0])
        n = self.Row * self.Col
        self.segment_tree = SegTree(n)
        for r in range(self.Row):
            for c in range(self.Col):
                ID = r * self.Col + c
                self.segment_tree.update(ID, matrix[r][c])

    def update(self, row: int, col: int, val: int) -> None:
        ID = row * self.Col + col
        self.matrix[row][col] = val
        self.segment_tree.update(ID, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            ID1 = r * self.Col + col1
            ID2 = r * self.Col + col2
            res += self.segment_tree.query(ID1, ID2)
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
