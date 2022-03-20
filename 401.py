class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def count_binary(n):
            count = 0

            while n > 0:
                count += n & 1
                n = n >> 1

            return count

        res = []
        for i in range(12):
            for j in range(60):
                if count_binary(i) + count_binary(j) == num:
                    res.append(str(i) + ':' + str(j).zfill(2))

        return res


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [1, 2, 4, 8, 0, 0, 0, 0, 0, 0]
        minutes = [0, 0, 0, 0, 1, 2, 4, 8, 16, 32]
        res = []

        def backtrack(num, index, hour, minute):
            if hour > 11 or minute > 59:
                return None

            if num == 0:
                res.append(str(hour) + ':' + str(minute).zfill(2))
                return None

            for i in range(index, 10):
                backtrack(num - 1, i + 1, hour + hours[i], minute + minutes[i])

        backtrack(num, 0, 0, 0)
        return res
