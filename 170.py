from collections import defaultdict
class TwoSum:

    def __init__(self):
        self.table = defaultdict(int)

    def add(self, number: int) -> None:
        self.table[number] += 1

    def find(self, value: int) -> bool:
        for k, v in self.table.items():
            if value - k in self.table:
                if value - k == k:
                    if v > 1: return True

                else:
                    if self.table[value - k] > 0:
                        return True

        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)