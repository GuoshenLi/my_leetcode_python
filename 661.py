class Solution(object):
    def imageSmoother(self, M):
        row = len(M)
        col = len(M[0])
        ans = [[0] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                count = 0
                tmp = 0
                for nr in (r - 1, r, r + 1):
                    for nc in (c - 1, c, c + 1):
                        if 0 <= nr < row and 0 <= nc < col:
                            tmp += M[nr][nc]
                            count += 1

                ans[r][c] = tmp // count

        return ans

