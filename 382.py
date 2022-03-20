# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.array = []
        while head:
            self.array.append(head.val)
            head = head.next


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """

        return random.choice(self.array)



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 数据流当中有1， 2， 3， 4
# 1, 1的概率选择1
# 2, 1 / 2 的概率选择2，1 / 2的概率在1，2中不选择2
# 3, 1 / 3 的概率选择3，2 / 3的概率在1，2，3中不选择3
# 4, 1 / 4 的概率选择4，3 / 4的概率在1，2，3，4中不选择4


# 因此最终，选择1的概率：   1 * （1 / 2）*（2 / 3）*（3 / 4）
# 因此最终，选择2的概率： （1 / 2）*（2 / 3）*（3 / 4）
# 因此最终，选择3的概率： （1 / 3）*（3 / 4）
# 因此最终，选择4的概率： （1 / 4）

# 蓄水池抽样
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        index = 1
        res = None

        cur = self.head
        while cur:
            if random.randint(1, index) == index:
                res = cur.val

            cur = cur.next
            index += 1

        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()