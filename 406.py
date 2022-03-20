from typing import List
# 第一个元素按降序排列，那么每个元素前面的元素个数就是大于等于它的元素数量
# 楼主的解释很棒！但是这里稍微有点没有解释清楚，“按照第二个元素正向排序，我们希望 k 大的尽量在后面，减少插入操作的次数。”
# 不止是为了减少插入次数，也是为了保证正确性。
# 举个例子，在身高一样，k不一样的时候，譬如[5,2]和[5,3], 对于最后排完的数组，[5,2]必然在[5,3]的前面。
# 所以如果遍历的时候[5,3]在前面，等它先插入完，这个时候它前面会有3个大于等于它的数组对，遍历到[5,2]的时候，
# 它必然又会插入[5,3]前面（因为它会插入链表索引为2的地方），这个时候[5,3]前面就会有4个大于等于它的数组对了，这样就会出错。

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        ans = list()
        for person in people:
            ans.insert(person[1], person)

        return ans


print(Solution().reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))