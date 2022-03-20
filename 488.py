from functools import lru_cache
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        res = self.dfs(board, hand)
        return res if res != float('+inf') else -1


    @lru_cache(None)
    def dfs(self, board: str, hand: str) -> int:

        board = self.squeeze_string(board)
        if not board: return 0
        if not hand: return float('+inf')

        MIN = float('+inf')
        #----尝试每个位置，每个颜色

        for i in range(len(board) + 1):
            for j in range(len(hand)):
                nxt_hand = hand[:j] + hand[j+1:]
                MIN = min(MIN, 1 + self.dfs(board[:i] + hand[j] + board[i:], nxt_hand))
        return MIN



    def squeeze_string(self, board):
        while True:
            left_bound, right_bound = self.canEliminate(board)
            if left_bound != -1 and right_bound != -1:
                board = board[:left_bound] + board[right_bound + 1:]
            else:
                return board



    def canEliminate(self, board):
        left = right = 0
        while right < len(board):
            while right < len(board) and board[left] == board[right]:
                right += 1

            if right - left >= 3:
                return left, right - 1

            left = right

        return -1, -1



solution = Solution()
print(solution.findMinStep(board = "WWRRBBWW", hand = "WRBRW"))