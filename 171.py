class Solution:
    def titleToNumber(self, s: str) -> int:


        table = {
            'Z': 26, 'Y': 25,
            'X': 24, 'W': 23, 'V': 22, 'U': 21,
            'T': 20, 'S': 19, 'R': 18, 'Q': 17,
            'P': 16, 'O': 15, 'N': 14, 'M': 13,
            'L': 12, 'K': 11, 'J': 10, 'I': 9,
            'H': 8, 'G': 7, 'F': 6, 'E': 5,
            'D': 4, 'C': 3, 'B': 2, 'A': 1
        }
        res = 0
        for char in s:
            res = res * 26 
            res = res + table[char]
        return res