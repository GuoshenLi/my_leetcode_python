from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [item[0] for item in count.most_common(k)]




import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = [(val, key) for key, val in count.items()]

        heap = count[:k]
        heapq.heapify(heap)

        for i in range(k, len(count)):
            if count[i][0] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, count[i])


        return [item[1] for item in heap]




from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_nums = list(Counter(nums).items()) # [(num, times)]
        target_index = len(freq_nums) - k
        left, right = 0, len(freq_nums) - 1
        while True:
            index = self.partition(freq_nums, left, right)
            if target_index == index:
                return list(map(lambda x: x[0], freq_nums[index:]))
            elif target_index > index:
                left = index + 1

            else:
                right = index - 1





    def partition(self, nums, left, right):
        tmp = nums[left]
        while left < right:
            while left < right and nums[right][1] >= tmp[1]:
                right -= 1
            nums[left] = nums[right]

            while left < right and nums[left][1] <= tmp[1]:
                left += 1

            nums[right] = nums[left]

        nums[left] = tmp
        return left


from collections import defaultdict


class Solution:

    def partition(self, nums, left, right):

        i = randint(left, right)
        nums[left], nums[i] = nums[i], nums[left]

        le = left + 1
        ge = right

        '''

            nums = [7, -1, 2, 5, 8, 9, 10]


                  left.             le        
                                 ge

        '''

        while True:
            while le <= ge and nums[le][1] < nums[left][1]:
                le += 1

            while le <= ge and nums[ge][1] > nums[left][1]:
                ge -= 1

            if le >= ge:
                break

            nums[le], nums[ge] = nums[ge], nums[le]
            le += 1
            ge -= 1

        nums[left], nums[ge] = nums[ge], nums[left]

        return ge

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        counter = list(counter.items())  # [(num, times)]
        print(counter)
        left = 0
        right = len(counter) - 1
        k = len(counter) - k
        while True:

            mid = self.partition(counter, left, right)
            if mid == k:
                return list(map(lambda x: x[0], counter[mid:]))
            elif mid > k:
                right = mid - 1
            else:
                left = mid + 1


print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))