class Solution:
    def compress(self, chars: List[str]) -> int:

        # 原地解决
        if len(chars) == 1: return 1

        left = 0
        right = 0
        index = 0

        while right < len(chars):
            while right < len(chars) and chars[left] == chars[right]:
                right += 1

            if right - left > 1:
                chars[index] = chars[left]
                index += 1
                count = str(right - left)
                for c in count:
                    chars[index] = c
                    index += 1
            else:
                chars[index] = chars[left]
                index += 1

            left = right

        return index