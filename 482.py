class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '')

        mod = len(S) % K
        full = len(S) // K

        res = ''
        if mod != 0:
            res += S[:mod]
            res += '-'

        for i in range(full):
            res += S[mod + K * i: mod + K * (i + 1)]
            res += '-'

        return res.upper()[:-1]
