from typing import List
class Solution:

    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)

        res = []

        def backtrace(idx: int, cur_res: int, pre_add: int, tmp: List) -> None:
            if idx == n:
                if cur_res == target:
                    res.append(''.join(tmp))
                    return None


            for i in range(idx, n):
                x_str = num[idx: i + 1]
                x = int(x_str)

                if idx == 0:
                    tmp.append(x_str)        #相当于只能是‘+’
                    backtrace(i + 1, x, x, tmp)
                    tmp.pop()
                else:
                    tmp.append('+' + x_str)
                    backtrace(i + 1, cur_res + x, x, tmp)
                    tmp.pop()

                    tmp.append('-' + x_str)
                    backtrace(i + 1, cur_res - x, -x, tmp)
                    tmp.pop()

                    tmp.append('*' + x_str)
                    backtrace(i + 1, cur_res - pre_add + pre_add * x, pre_add * x, tmp)
                    # 难在这里
                    tmp.pop()

                # 只要算出来x == 0，算完+ - * 以后就可以终止了 因为
                # 再后来的01 02 011 全都是不符合的。因此可以终止
                if x == 0:      #是个坑
                    return None

        backtrace(0, 0, 0, [])
        return res



# 2021-12-29 暴力解法
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def dfs(index, start, tmp):
            if start == n:
                if eval(''.join(tmp)) == target:
                    res.append(''.join(tmp[:]))
                return None
            if index == 0:
                for end in range(start, n):
                    slice_ = num[start: end + 1]
                    if end != start and slice_[0] == '0':
                        continue
                    tmp.append(slice_)
                    dfs(index + 1, end + 1, tmp)
                    tmp.pop()

            else:
                for end in range(start, n):

                    slice_ = num[start: end + 1]
                    if end != start and slice_[0] == '0':
                        continue
                    tmp.append('-' + slice_)
                    dfs(index + 1, end + 1, tmp)
                    tmp.pop()

                    tmp.append('+' + slice_)
                    dfs(index + 1, end + 1, tmp)
                    tmp.pop()

                    tmp.append('*' + slice_)
                    dfs(index + 1, end + 1, tmp)
                    tmp.pop()

        dfs(0, 0, [])
        return res


print(Solution().addOperators(num = '105', target = 5))