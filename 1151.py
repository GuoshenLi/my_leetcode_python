class Solution:
    def minSwaps(self, data: List[int]) -> int:

        # 求解滑动窗口中的最多的1的个数

        num_ones = data.count(1)
        max_ones = 0
        count_ones = 0
        for i in range(num_ones):
            if data[i] == 1:
                count_ones += 1

        max_ones = max(max_ones, count_ones)

        for i in range(num_ones, len(data)):
            if data[i - num_ones] == 1:
                count_ones -= 1

            if data[i] == 1:
                count_ones += 1

            max_ones = max(max_ones, count_ones)

        return num_ones - max_ones