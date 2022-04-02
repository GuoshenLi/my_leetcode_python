from collections import defaultdict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.times = 1
        self.prev = None
        self.next = None

class Doubly_Linked_List:
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

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.min_time = float('+inf')

        self.key_2_node = {} # key: key, value: node
        self.times_2_dll = defaultdict(Doubly_Linked_List)  # key: times, value: dll

    def get(self, key: int) -> int:
        if self.capacity == 0: return -1
        if key not in self.key_2_node: return -1
        node = self.key_2_node[key]
        res = node.val
        times = node.times
        self.times_2_dll[times].delete(node)

        if times == self.min_time and self.times_2_dll[times].head.next == self.times_2_dll[times].tail:
            self.min_time += 1

        times += 1
        node.times = times
        dll = self.times_2_dll[times]
        dll.add_behind(dll.head, node)

        return res

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.key_2_node:
            node = self.key_2_node[key]
            node.val = value # 更新
            times = node.times

            self.times_2_dll[times].delete(node)
            if times == self.min_time and self.times_2_dll[times].head.next == self.times_2_dll[times].tail:
                self.min_time += 1

            times += 1
            node.times = times
            dll = self.times_2_dll[times]
            dll.add_behind(dll.head, node)
        else:
            if self.count < self.capacity:
                self.count += 1
                new_node = Node(key, value)
                dll = self.times_2_dll[new_node.times]
                dll.add_behind(dll.head, new_node)

                self.key_2_node[key] = new_node

            else:
                dll = self.times_2_dll[self.min_time]
                del self.key_2_node[dll.tail.prev.key]
                dll.delete(dll.tail.prev)

                new_node = Node(key, value)
                dll = self.times_2_dll[new_node.times]
                dll.add_behind(dll.head, new_node)

                self.key_2_node[key] = new_node

            self.min_time = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)