import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        intervals.sort(key = lambda x: x[0])
        heap = [intervals[0][1]]
        # 截止目前为止 会议的所有结束时间
        count = 1

        for interval in intervals[1:]:
            if interval[0] < heap[0]:
                count += 1
            else:
                heapq.heappop(heap)

            heapq.heappush(heap, interval[1])


        return count

