from collections import defaultdict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.time_used = 1

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

    def add_behind(self, cur, node):
        node.prev = cur
        node.next = cur.next

        cur.next.prev = node
        cur.next = node


    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None

class LFUCache:

    def __init__(self, capacity: int):
        self.time_to_lru = defaultdict(Double_linked_list) # 每一个使用次数都是一个lru
        self.capacity = capacity
        self.count = 0
        # key: key, value: 直接对应dll的节点
        self.table = {}
        self.min_time = float('+inf')

    def get(self, key: int) -> int:
        if key not in self.table: return -1
        if self.capacity == 0: return -1
        # 在
        node = self.table[key]
        res = node.val

        time = node.time_used
        dll = self.time_to_lru[time]
        dll.delete(node)

        if self.min_time == time and dll.head.next == dll.tail:
            self.min_time += 1


        node.time_used += 1
        dll_next = self.time_to_lru[time + 1]
        dll_next.add_behind(dll_next.head, node)

        return res

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return None
        if key in self.table:
            node = self.table[key]
            time = node.time_used
            dll = self.time_to_lru[time]
            dll.delete(node)

            if self.min_time == node.time_used and dll.head.next == dll.tail:
                self.min_time += 1


            node.time_used += 1
            node.val = value
            dll_next = self.time_to_lru[time + 1]
            dll_next.add_behind(dll_next.head, node)

        else:
            # 不在
            if self.count < self.capacity:
                # 直接插入
                new_node = Node(key, value)
                time = new_node.time_used
                dll = self.time_to_lru[time]
                dll.add_behind(dll.head, new_node)

                self.table[key] = new_node
                self.count += 1

            else:
                # 满了 只能先删除
                # 记录一个最小使用次数
                dll = self.time_to_lru[self.min_time]
                del self.table[dll.tail.prev.key]
                dll.delete(dll.tail.prev)

                new_node = Node(key, value)
                time = new_node.time_used
                dll = self.time_to_lru[time]
                dll.add_behind(dll.head, new_node)

                self.table[key] = new_node

            self.min_time = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



from collections import defaultdict
class Node:
    def __init__(self, key, val):
        self.times = 1
        self.key = key
        self.val = val



class Doubly_linked_list:
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



    def add_behind(self, cur, node):

        node.prev = cur
        node.next = cur.next

        cur.next.prev = node
        cur.next = node



    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None






class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.table_dll = defaultdict(Doubly_linked_list)   # key: 使用次数 value: dll
        self.key_val_table = {}
        self.min_use = 0

    def get(self, key: int) -> int:
        if key not in self.key_val_table:
            return -1
        if self.capacity == 0: return -1

        node = self.key_val_table[key]
        val = node.val
        times = node.times
        dll = self.table_dll[times]
        dll.delete_node(node)

        if self.min_use == times and dll.head.next == dll.tail.prev:
            self.min_use = times + 1
        node.times += 1

        next_dll = self.table_dll[times + 1]
        next_dll.add_behind(next_dll.head, node)


        return val


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return None
        if key in self.key_val_table:
            node = self.key_val_table[key]
            times = node.times
            dll = self.table_dll[times]
            dll.delete_node(node)
            if self.min_use == times and dll.head.next == dll.tail.prev:
                self.min_use = times + 1

            node.val = value
            node.times += 1
            next_dll = self.table_dll[times + 1]
            next_dll.add_behind(next_dll.head, node)

        else:
            if self.length < self.capacity:
                self.length += 1
                new_node = Node(key, value)
                self.key_val_table[key] = new_node
                dll = self.table_dll[1]
                dll.add_behind(dll.head, new_node)



            else:
                dll = self.table_dll[self.min_use]
                del self.key_val_table[dll.tail.prev.key]
                dll.delete_node(dll.tail.prev)
                new_node = Node(key, value)
                self.key_val_table[key] = new_node
                dll = self.table_dll[1]
                dll.add_behind(dll.head, new_node)

            self.min_use = 1






# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
lfu.get(1)
lfu.put(3, 3)
lfu.get(2)
lfu.get(3)
lfu.put(1)
lfu.get(3)
lfu.get(4)


# ["LFUCache", "put", "put", "get", "put", "get", "get", "put"]
# [[2],        [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4]]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)