# 暴力法
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = nums[:]

    def reset(self):
        self.array = self.original[:]
        return self.original

    def shuffle(self):
        tmp = self.array[:]
        for i in range(len(self.array)):
            index = random.randrange(len(tmp))
            self.array[i] = tmp.pop(index)

        return self.array


# 洗牌法
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = nums[:]

    def reset(self):
        self.array = self.original[:]
        return self.original

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array

