class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        return min(len(set(candyType)),len(candyType)//2)

print(Solution().distributeCandies(candyType = [1,1,2,2,3,3]))