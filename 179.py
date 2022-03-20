class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(str, nums))
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        while nums and nums[0] == '0':
                nums.pop()

        return ''.join(nums) if nums else '0'



from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums) -> str:
        nums = list(map(str, nums))
        # 匿名函数的返回值应为1（应该交换位置，将b放到前面）或-1或0（两者相等）
        nums = sorted(nums, key=cmp_to_key(lambda a, b: 1 if int(b+a) > int(a+b) else -1))
        while nums and nums[0] == '0':
            nums.pop(0)
        return "".join(nums) if nums else '0'