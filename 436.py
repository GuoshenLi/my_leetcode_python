# 找第一个大于等于它的数 如果找不到 就返回-1 这种情况小于单独拿出来
# 因为小于的话肯定不是答案 因此可以left = mid + 1

def binary_search(num, target):

    if target > num[-1]:
        return -1

    left = 0
    right = len(num) - 1

    while left < right:
        mid = (left + right) // 2
        if num[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


print(binary_search(num = [1,2,4,6,8,9,10,11,12], target=3))

# 按照第一个元素start排序 并且记录原始序号
# 感觉区间题目通常都要排序
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        startlist = []
        size = len(intervals)
        for index, [s, v] in enumerate(intervals):
            startlist.append([s, index])

        startlist.sort(key=lambda x: x[0])

        def binary_search(target):
            left = 0
            right = size - 1
            if target > startlist[right][0]:
                return -1
            # 找第一个大于等于它的数
            while left < right:
                mid = (left + right) // 2
                if startlist[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid

            return startlist[left][1]

        res = []
        for s, v in intervals:
            res.append(binary_search(v))
        return res


