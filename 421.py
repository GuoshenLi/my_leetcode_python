# 典型的字典树
from typing import List
class Trie_node:
    def __init__(self):
        self.next = [None for i in range(2)]
        self.is_num = False

class Trie_Tree:
    def __init__(self):
        self.root = Trie_node()

    def insert(self, num):
        # 一个number有31位
        # 从最高位开始取digit
        cur_node = self.root
        for i in range(30, -1, -1):
            digit = (num >> i) & 1
            if not cur_node.next[digit]:
                cur_node.next[digit] = Trie_node()
            cur_node = cur_node.next[digit]

        cur_node.is_num = True

    def query(self, num):
        cur_node = self.root
        res = 0
        for i in range(30, -1, -1):
            digit = (num >> i) & 1
            if digit == 1:
                if cur_node.next[0]:
                    res = (res << 1) + 1
                    cur_node = cur_node.next[0]
                else:
                    res = res << 1
                    cur_node = cur_node.next[1]
            else:
                if cur_node.next[1]:
                    res = (res << 1) + 1
                    cur_node = cur_node.next[1]
                else:
                    res = res << 1
                    cur_node = cur_node.next[0]

        return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        tree = Trie_Tree()
        res = 0

        for num in nums:
            tree.insert(num)

        for num in nums:
            res = max(res, tree.query(num))

        return res


print(Solution().findMaximumXOR(nums = [3,10,5,25,2,8]))