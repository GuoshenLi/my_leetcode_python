class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortns = []
        res = []
        for n in reversed(nums):
            idx = bisect.bisect_left(sortns, n)
            res.append(idx)
            sortns.insert(idx,n)
        return res[::-1]



class Item:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        items = [Item(nums[i], i) for i in range(n)]

        count = [0 for i in range(n)]

        self.merge_sort(items, 0, n - 1, count)

        return count

    def merge_sort(self, items, low, high, count):

        if low >= high: return None
        mid = (low + high) // 2
        self.merge_sort(items, low, mid, count)
        self.merge_sort(items, mid + 1, high, count)
        self.merge(items, low, mid, high, count)


    def merge(self, items, low, mid, high, count):
        # 左有序数组
        # 右有序数组

        left = low
        right = mid + 1
        rightCounter = 0
        # 这段代码真的太巧妙了！！牛逼！！
        # 例如：左有序数组 [2, 4, 5, 6]
        #      右有序数组 [2, 3, 7, 8]
        # 其实就是要去统计对于每一个左有序数组的数
        # 与右有序数组进行组合的时候，所对应的逆序对的个数是多少
        # 也就是说对于每一个左有序数组中的数在右有序数组中有多少个比当前左有序数组中的数小


        # 这几个题目都一样的 全都一样的 遍历left 然后去动right
        # 这几个题目都是这么算的
        while left <= mid:
            while right <= high and items[right].val < items[left].val:
                right += 1

            count[items[left].idx] += (right - (mid + 1))
            left += 1




        left = low
        right = mid + 1
        tmp = []

        # 这是merge 操作
        while left <= mid and right <= high:
            if items[right].val < items[left].val:
                tmp.append(items[right])
                right += 1

            else:
                tmp.append(items[left])
                left += 1


        while left <= mid:
            tmp.append(items[left])
            left += 1

        while right <= high:
            tmp.append(items[right])
            right += 1

        items[low: high + 1] = tmp

