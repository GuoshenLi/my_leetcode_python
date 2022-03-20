class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        # 用int可以去除前导零
        len1 = len(ver1)
        len2 = len(ver2)

        if len1 > len2:
            ver2.extend(['0'] * (len1 - len2))

        if len2 > len1:
            ver1.extend(['0'] * (len2 - len1))

        for i in range(max(len1, len2)):
            if int(ver1[i]) > int(ver2[i]):
                return 1
            elif int(ver1[i]) < int(ver2[i]):
                return - 1

        return 0

print(Solution().compareVersion(version1 = "1", version2 = "1.1"))
