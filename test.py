class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def creat_linklist(li):
    node = Node(li[0])
    head = node

    for item in li[1:]:
        node = Node(item)
        node.next = head
        head = node

    return head

def print_lk(head):
    while head:
        print(head.val, end = ",")
        head = head.next

def creat_linklist_back(li):
    node = Node(li[0])
    head = node
    tail = node

    for item in li[1:]:
        node = Node(item)
        tail.next = node
        tail = node

    return head

if __name__ == "__main__":
    li = [1,2,3,4,5]

    head = creat_linklist_back(li)
    print_lk(head)





