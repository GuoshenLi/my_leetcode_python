class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        lookup = {
            "6" : "9",
            "9" : "6",
            "8" : "8",
            "1" : "1",
            "0" : "0"
        }
        rotated_num = ""
        for a in num:
            if a in lookup:
                rotated_num += lookup[a]
            else:
                return False
        return rotated_num[::-1] == num