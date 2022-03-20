# 暴力法 超时
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.d=nums

    def update(self, i: int, val: int) -> None:
        self.d[i]=val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.d[i:j+1])




# 线段树模版 背诵
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0 for _ in range(4 * self.n)]
        self.__build_tree(0, 0, self.n - 1)

    def __build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
            return None

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        self.__build_tree(left_child, start, mid)
        self.__build_tree(right_child, mid + 1, end)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]

        return None

    def __update_val(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            self.nums[idx] = val
            return None

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if idx <= mid:
            self.__update_val(left_child, start, mid, idx, val)
        else:
            self.__update_val(right_child, mid + 1, end, idx, val)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]

        return None

    def __query_val(self, node, start, end, query_left, query_right):
        if start > query_right or end < query_left: return 0
        elif query_left <= start and query_right >= end: return self.tree[node]
        elif start == end: return self.tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_sum = self.__query_val(left_child, start, mid, query_left, query_right)
        right_sum = self.__query_val(right_child, mid + 1, end, query_left, query_right)

        return left_sum + right_sum


    def update(self, index: int, val: int) -> None:
        self.__update_val(0, 0, self.n - 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.__query_val(0, 0, self.n - 1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)