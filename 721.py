from collections import defaultdict


class Solution:

    def find(self, x, root):
        while root[x] != -1:
            x = root[x]
        return x

    def union(self, x, y, root, rank):
        x_root = self.find(x, root)
        y_root = self.find(y, root)

        if x_root == y_root:
            return False

        else:
            if rank[x_root] > rank[y_root]:
                root[y_root] = x_root

            elif rank[y_root] > rank[x_root]:
                root[x_root] = y_root

            else:
                root[x_root] = y_root
                rank[y_root] += 1

            return True

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        root = [-1 for _ in range(n)]
        rank = [0 for _ in range(n)]

        match_table = {}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in match_table:
                    match_table[email] = i
                    # match_table 去重
                else:
                    self.union(i, match_table[email], root, rank)

        # [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]


        # "johnsmith@mail.com": 0, "john00@mail.com": 0
        # "johnnybravo@mail.com": 1
        # "johnsmith@mail.com" (2 与 0 合并)
        # "john_newyork@mail.com": 2
        # "mary@mail.com": 3
        #           index:  [ 0,  1, 2,  3]
        # 合并完以后的parent: [-1, -1, 0, -1]



        dic = defaultdict(list)

        for key, val in match_table.items():
            dic[self.find(val, root)].append(key)

        # number 0: email
        # number 1: email

        res = []
        for key, val in dic.items():
            name = accounts[key][0]
            res.append([name] + sorted(val))

        return res


# 个人觉得能写出并查集已经通过一大半了！！
Solution().accountsMerge(accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])