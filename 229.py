class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count_dict = {}
        for item in nums:
            count_dict[item] = count_dict.get(item, 0) + 1

        res = []
        for k, v in count_dict.items():
            if v > len(nums) / 3:
                res.append(k)

        return res

# 如果至多选一个代表，那他的票数至少要超过一半（⌊ 1/2 ⌋）的票数；
#
# 如果至多选两个代表，那他们的票数至少要超过 ⌊ 1/3 ⌋ 的票数；
#
# 如果至多选m个代表，那他们的票数至少要超过 ⌊ 1/(m+1) ⌋ 的票数。



class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []

        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1

            elif candidate2 == n:
                count2 += 1

            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                res.append(c)

        return res