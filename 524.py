class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        ans = ''
        for string_in_dict in dictionary:

            i = 0
            j = 0
            # 双指针判断是否能删除 也就是判断是否是子序列

            while i < len(s) and j < len(string_in_dict):
                if s[i] == string_in_dict[j]:
                    i += 1
                    j += 1
                else:
                    i += 1

            if j == len(string_in_dict):
                if len(string_in_dict) > len(ans) or len(string_in_dict) == len(ans) and string_in_dict < ans:
                    # 同样长度才能够利用 str1 > str2 判断字典序
                    ans = string_in_dict

        return ans


