class MyCircularQueue:
    # 维护一个长度为k的数组，count计算数组中有效个数，head指向队列的头，涉及到head的运算 + 1 or + count都要取余数

    def __init__(self, k: int):
        self.cap = k
        self.q = [0] * k
        self.count = 0
        self.head = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.cap:
            return False
        self.q[(self.head + self.count) % self.cap] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        self.head = (self.head + 1) % self.cap
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.q[(self.head + self.count - 1) % self.cap]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.cap

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()