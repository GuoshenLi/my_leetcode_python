class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.tmp = [num for nums in vec for num in nums]
        self.pointer = 0

    def next(self) -> int:
        res = self.tmp[self.pointer]
        self.pointer += 1
        return res

    def hasNext(self) -> bool:
        return self.pointer < len(self.tmp)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
