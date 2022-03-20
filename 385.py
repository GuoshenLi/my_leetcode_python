# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# s= "{22:233,1:32}"
# s = "[1,2,3,4,5]"
# s = "5*6"
# s = "(1,2,3,4,5)"
# print(eval(s))

# 只用到add
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def dfs(elem):
            if isinstance(elem, int):
                return NestedInteger(elem)
            li = NestedInteger()  # 这个对象为空时是一个空列表
            for i in elem:
                li.add(dfs(i))
            return li

        return dfs(eval(s))




