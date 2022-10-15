class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:


        res = []

        for i in range(len(favoriteCompanies)):
            flag = False
            for j in range(len(favoriteCompanies)):
                if i != j:
                    if set(favoriteCompanies[i]) & set(favoriteCompanies[j]) == set(favoriteCompanies[i]):
                        flag = True
                        break

            if flag == False:
                res.append(i)

        return res