
# 暴力解法

class Solution(object):
    def isAlienSorted(self, words, order):

        order_map = dict()
        for i in range(len(order)):
            order_map[order[i]] = i


        for i in range(len(words) - 1):
            cur_word = words[i]
            next_word = words[i + 1]

            min_length = min(len(cur_word), len(next_word))

            for j in range(min_length):
                if cur_word[j] != next_word[j]:
                    if order_map[cur_word[j]] > order_map[next_word[j]]:
                        return False

                    else:
                        break

            else:

                if len(cur_word) > len(next_word):
                    return False

        return True









