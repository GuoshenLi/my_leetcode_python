from collections import defaultdict
from random import choice
class RandomizedCollection:

    def __init__(self):
        self.table = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:

        index = len(self.list)
        self.list.append(val)
        self.table[val].add(index)

        return len(self.table[val]) == 1


    def remove(self, val: int) -> bool:
        if val not in self.table: return False
        index = self.table[val].pop()
        if len(self.table[val]) == 0:
            del self.table[val]

        if index == len(self.list) - 1:
            self.list.pop()
        else:

            last_item = self.list[-1]
            self.list[-1], self.list[index] = self.list[index], self.list[-1]
            self.table[last_item].remove(len(self.list) - 1)
            self.table[last_item].add(index)
            self.list.pop()


        return True

    def getRandom(self) -> int:

        return choice(self.list)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()