### 找第三大数值 不是元素
### 若第k个元素 则用快速选择

# 的确也是O(n)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        mock=list(set(nums))
        if len(mock)<3:
            return max(mock)
        mock.remove(max(mock))
        mock.remove(max(mock))
        return max(mock)

# 三指针
class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        First_Max = Second_Max = Third_Max = float('-inf')

        for num in nums:
            if First_Max < num:
                First_Max, Second_Max, Third_Max = num, First_Max, Second_Max
            elif Second_Max < num < First_Max:
                Second_Max, Third_Max = num, Second_Max
            elif Third_Max < num < Second_Max:
                Third_Max = num

        return First_Max if Third_Max == float('-inf') else Third_Max