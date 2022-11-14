#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# 递归更好做
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.iterate = []
        self.pointer = 0

        def dfs(nestedList):

            for item in nestedList:
                if item.isInteger():
                    self.iterate.append(item.getInteger())
                else:
                    dfs(item.getList())

        dfs(nestedList)
        self.length = len(self.iterate)

    def next(self) -> int:
        val = self.iterate[self.pointer]
        self.pointer += 1
        return val

    def hasNext(self) -> bool:
        return self.pointer < self.length









# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.pointer = 0

        def dfs(ls):
            if not ls: return []
            res = []
            for item in ls:
                if item.isInteger():
                    res.append(item.getInteger())
                else:
                    res.extend(dfs(item.getList()))
            return res

        self.res = dfs(nestedList)


    def next(self) -> int:
        result = self.res[self.pointer]
        self.pointer += 1
        return result


    def hasNext(self) -> bool:
        return self.pointer < len(self.res)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())