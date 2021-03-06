# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        #用列表存储迭代器的值
        self.nums = []
        #目前遍历到列表的索引值
        self.index = 0
        #首先遍历一遍迭代器，存储数据，以便返回peek()函数的值
        while iterator.hasNext():
            self.nums.append(iterator.next())
        #总的列表的元素个数，目的是为了hasNext()函数的判断
        self.lenth = len(self.nums)

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """

        return self.nums[self.index]

    def next(self):
        """
        :rtype: int
        """
        #保存当前值
        value = self.nums[self.index]
        #索引加1，目的为了返回下一次值
        self.index += 1
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        #索引值判断是否遍历完成
        return self.index < self.lenth



# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = iterator.next()
        self._hasNext = iterator.hasNext()

    def peek(self):
        return self._next

    def next(self):
        ret = self._next
        self._hasNext = self.iterator.hasNext()
        self._next = self.iterator.next() if self._hasNext else 0
        return ret

    def hasNext(self):
        return self._hasNext
