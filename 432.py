class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.keys_contained = set()


class Double_linked_list:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('+inf'))

        self.head.next = self.tail
        self.tail.prev = self.head


    def add_front(self, cur, node):
        node.prev = cur.prev
        node.next = cur

        cur.prev.next = node
        cur.prev = node

    def add_next(self, cur, node):
        node.next = cur.next
        node.prev = cur

        cur.next.prev = node
        cur.next = node


    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll = Double_linked_list()

        # k: key; v: the node
        self.table = {}

        # 每进行一步操作 都要维护
        # 1: self.dll连接
        # 2: node.keys_contained
        # 3: self.table

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if not key: return None
        if key not in self.table:
            # 肯定要新增为1
            # 但是还要判断有没有self.dll 中有没有值为1的节点
            if self.dll.head.next.val != 1:
                # 没有
                new_node = Node(1)
                new_node.keys_contained.add(key) # 1
                self.dll.add_next(self.dll.head, new_node) # 2
                self.table[key] = new_node # 3


            else:
                # 有只为1的节点
                node = self.dll.head.next
                node.keys_contained.add(key) # 2
                self.table[key] = node # 3

        else: # 已经在self.table 中
            # 要增加1, 看连续不连续
            cur = self.table[key]
            if cur.val + 1 == cur.next.val:
                # 连续
                cur.next.keys_contained.add(key) # 2
                self.table[key] = cur.next # 3

                cur.keys_contained.remove(key) # 删除
                if len(cur.keys_contained) == 0: # 每当remove一次都要判断
                    self.dll.delete(cur)

            else:
                # 不连续
                # 因此要新建

                new_node = Node(cur.val + 1)
                self.dll.add_next(cur, new_node) # 1
                new_node.keys_contained.add(key) # 2
                self.table[key] = new_node # 3

                cur.keys_contained.remove(key) # 删除
                if len(cur.keys_contained) == 0: # 每当remove一次都要判断
                    self.dll.delete(cur)


    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """

        if key not in self.table: return None

        cur = self.table[key]
        if cur.val == 1:
            # 要删除
            cur.keys_contained.remove(key) # 2
            if len(cur.keys_contained) == 0:
                self.dll.delete(cur) # 1

            del self.table[key] # 3

        else:
            # 数量大于1
            # 判断连续不连续
            if cur.val - 1 == cur.prev.val:
                # 连续
                # 增加
                cur.prev.keys_contained.add(key) # 2
                self.table[key] = cur.prev # 3

                # 删除
                cur.keys_contained.remove(key) # 2
                if len(cur.keys_contained) == 0:
                    self.dll.delete(cur) # 1

            else:
                # 不连续
                new_node = Node(cur.val - 1)
                # 增加
                self.dll.add_front(cur, new_node) # 1
                new_node.keys_contained.add(key) # 2
                self.table[key] = new_node # 3

                # 删除
                cur.keys_contained.remove(key) # 2
                if len(cur.keys_contained) == 0:
                    self.dll.delete(cur)


    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """

        return '' if self.dll.head.next == self.dll.tail else next(iter(self.dll.tail.prev.keys_contained))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return '' if self.dll.head.next == self.dll.tail else next(iter(self.dll.head.next.keys_contained))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()