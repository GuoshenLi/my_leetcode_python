from random import choice

# 数组 + 哈希表
# 哈希表存数组中每个数字的下标
# 数组存数字
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False
        # 一定要交换到最后 然后pop才可以实现0(1)的时间复杂度
        idx = self.dict[val]
        last_item = self.list[-1]

        self.list[-1], self.list[idx] = self.list[idx], self.list[-1]
        self.list.pop()
        self.dict[last_item] = idx
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()