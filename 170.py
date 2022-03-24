from collections import defaultdict
class TwoSum(object):
    def __init__(self):
        self.count_table = defaultdict(int)


    def add(self, number):
        self.count_table[number] += 1


    def find(self, value):
        for num in self.count_table.keys():
            target = value - num
            if target == num:
                if self.count_table[target] > 1:
                    return True

            else:
                if target in self.count_table:
                    return True

        return False




