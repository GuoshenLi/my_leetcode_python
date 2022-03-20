class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        dict1 = {}
        dict2 = {}
        bull = 0
        cow = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1

            else:
                dict1[secret[i]] = dict1.get(secret[i], 0) + 1
                dict2[guess[i]] = dict2.get(guess[i], 0) + 1

        for i in dict1:
            if i in dict2:
                cow += min(dict1[i], dict2[i])

        return str(bull) + 'A' + str(cow) + 'B'
