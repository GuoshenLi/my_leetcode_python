class Solution:
    # 迭代的时候记录每一轮数组的第一个元素
    # 找规律

    def lastRemaining(self, n: int) -> int:
        res = 1
        step = 1
        remain = n
        is_delete_from_left = True
        while remain > 1:
            # 如果从左边开始或者从右边开始并且长度为奇数 才用更新
            if is_delete_from_left or remain % 2 == 1:
                res += step
            is_delete_from_left = not is_delete_from_left
            step = step * 2
            remain = remain // 2

        return res