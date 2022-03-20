# LRU 缓存
# 面试很喜欢这个题目
# 只有死背
# 哈希表 + 双向链表

# 背诵双向链表模版
class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class Double_linked_list:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

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

        node.next = None
        node.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # k: 关键字key, v: 对应的node
        self.table = {}
        self.dll = Double_linked_list()
        self.count = 0

    def get(self, key: int) -> int:

        if key not in self.table: return -1
        # 存在
        node = self.table[key]
        res = node.val

        # 移动到链表开头
        self.dll.delete(node)
        self.dll.add_next(self.dll.head, node)


        return res


    def put(self, key: int, value: int) -> None:
        if key in self.table:
            # 变换数值
            node = self.table[key]
            node.val = value
            # 删除
            self.dll.delete(node)
            # 再在队伍头部添加
            self.dll.add_next(self.dll.head, node)

        else:
            # 要插入了
            if self.count < self.capacity:
                # 可以插入
                self.count += 1
                new_node = Node(key, value)
                self.dll.add_next(self.dll.head, new_node)
                self.table[key] = new_node
            else:
                # 满了 要pop处最后一个
                delete_node = self.dll.tail.prev
                del self.table[delete_node.key]

                self.dll.delete(delete_node)
                new_node = Node(key, value)
                self.dll.add_next(self.dll.head, new_node)
                self.table[key] = new_node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



