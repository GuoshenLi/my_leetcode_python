import random


class Solution:
    def __init__(self, w: List[int]):
        self.len_w = len(w)
        self.presum = [0] * (self.len_w + 1)
        for i in range(1, self.len_w + 1):
            self.presum[i] = self.presum[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        num = random.randint(1, self.presum[-1])
        return self.binary_search(num) - 1

    def binary_search(self, num):
        left = 0
        right = self.len_w  # presum比w长度多1

        while left < right:
            mid = (left + right) // 2

            if self.presum[mid] < num:
                left = mid + 1
            else:
                right = mid

        return right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()