"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_map = {item.id: item for item in employees}

        def dfs(id):
            # 这个id 和其下面对应的重要程度之和

            res = id_map[id].importance
            for subordinate in id_map[id].subordinates:
                res += dfs(subordinate)
            return res

        return dfs(id)
