
# 用dict记录nums中每个元素出现的位置，
# 遍历哈希表，如果这个元素对应的频数为最大值,
# 就看它的长度为多少即可，然后取最短的长度

# 用dict记录nums中每个元素出现的位置，
# 度为出现位置最多的len，返
# 回拥有相同度的元素中，min（首末位置最+1）
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        loc_table = {}
        # 存储每一个元素对应的位置
        for i in range(len(nums)):
            if nums[i] in loc_table:
                loc_table[nums[i]].append(i)
            else:
                loc_table[nums[i]] = [i]

        max_freq = float('-inf')
        for k, v in loc_table.items():
            max_freq = max(max_freq, len(v))

        res = float('+inf')
        for k, v in loc_table.items():
            if len(v) == max_freq:
                res = min(res, (v[-1] - v[0] + 1))
                # 长度为 最后一个出现的位置 - 第一个出现的位置 + 1

        return res


