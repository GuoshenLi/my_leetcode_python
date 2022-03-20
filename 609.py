class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        aux = {}
        for path in paths:
            values = path.split(" ")
            for i in range(1,len(values)):
                name_cont = values[i].split("(")
                name_cont[1] = name_cont[1].replace(")","")
                l = values[0] + "/" + name_cont[0]
                if name_cont[1] in aux:
                    aux[name_cont[1]].append(l)
                else:
                    aux[name_cont[1]] = [l]

        res=[]
        for k, v in aux.items():
            if len(v) > 1:
                res.append(aux[k])
        return res