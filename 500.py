class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        array_1 = {"q","w","e","r","t","y","u","i","o","p","Q","W","E","R","T","Y","U","I","O","P"}
        array_2 = {"A","S","D","F","G","H","J","K","L","a","s","d","f","g","h","j","k","l"}
        array_3 = {"z","x","c","v","b","n","m","Z","X","C","V","B","N","M"}

        result = []
        for word in words:
            count_1 = 0
            count_2 = 0
            count_3 = 0
            length = len(word)
            for letter in word:
                if letter in array_1:
                    count_1 += 1
                if letter in array_2:
                    count_2 += 1
                if letter in array_3:
                    count_3 += 1
            if count_1==length or count_2==length or count_3 == length:
                result.append(word)
        return result


