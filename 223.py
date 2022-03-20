class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:


        first = (D - B) * (C - A)
        second = (G - E) * (H - F)

        left_bound = max(A, E)
        right_bound = min(C, G)

        upper_bound = min(D, H)
        lower_bound = max(B, F)

        if right_bound <= left_bound or upper_bound <= lower_bound:
            overlap = 0
        else:
            overlap = (right_bound - left_bound) * (upper_bound - lower_bound)

        return first + second - overlap

