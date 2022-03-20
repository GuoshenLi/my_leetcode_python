# 暴力法 一个大数组存储
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_set = [0 for i in range(1000001)]

    def add(self, key: int) -> None:
        self.my_set[key] = 1

    def remove(self, key: int) -> None:
        self.my_set[key] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.my_set[key] == 1




# 利用hash + 链表的方式存储 记住背诵！！
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.bucket_size = 1009
        self.bucket = [Linklist() for _ in range(self.bucket_size)]

    def add(self, key: int) -> None:
        self.bucket[key % self.bucket_size].add(key)

    def remove(self, key: int) -> None:
        self.bucket[key % self.bucket_size].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.bucket[key % self.bucket_size].exist(key)


class Linklist:
    # 一定要创建一个虚拟节点 否则很可能出错
    def __init__(self):
        self.dummy = Node(0)  # 创建虚拟节点 dummy
        self.head = self.dummy.next

    def add(self, val):
        if not self.exist(val):
            new_node = Node(val)
            self.dummy.next = new_node
            new_node.next = self.head
            self.head = self.dummy.next

    def remove(self, val):
        pre = self.dummy
        cur = self.head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                break

            cur = cur.next
            pre = pre.next
        self.head = self.dummy.next

    def exist(self, val):
        cur = self.head
        while cur:
            if val == cur.val:
                return True
            cur = cur.next

        return False


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)




#
class MyHashSet:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key):
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key):
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key):
        hashkey = self.hash(key)
        return key in self.table[hashkey]

