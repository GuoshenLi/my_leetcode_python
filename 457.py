# 虾皮笔试2021

class Solution:

    def circularArrayLoop(self, nums: List[int]) -> bool:
        getnext = lambda i: (i + nums[i]) % n
        n = len(nums)
        for i in range(n):
            # 快慢指针
            slow = i
            fast = getnext(i)
            # slow和fast仅仅是一个下标index

            # 这有点像链表中的while fast and fast.next:
            # 快指针每次走两步，因此要判断一下两步是不是都方向相同
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[getnext(fast)] > 0:
                if slow == fast:
                    # 环的长度不能为1
                    if slow == getnext(slow):
                        break
                    return True
                slow = getnext(slow)
                fast = getnext(getnext(fast))
        return False




class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n = len(nums)
        get_next = lambda i: (i + nums[i]) % n

        for i in range(n):
            slow = i
            fast = i

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[get_next(fast)] > 0:

                slow = get_next(slow)
                fast = get_next(get_next(fast))

                if slow == fast:
                    if slow == get_next(slow):
                        break
                    return True

        return False

# 加多一层判断就是 O(n)
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n = len(nums)
        get_next = lambda i: (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue
            slow = i
            fast = i

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[get_next(fast)] > 0:
                slow = get_next(slow)
                fast = get_next(get_next(fast))

                if slow == fast:
                    if slow == get_next(slow):
                        break
                    return True

            pointer = i
            while nums[pointer] * nums[get_next(pointer)] > 0:
                nums[pointer] = 0
                pointer = get_next(pointer)

        return False