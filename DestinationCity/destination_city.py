import sys 
from typing import List 

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pathDic = {}
        for path in paths:
            if path[0] in pathDic:
                pathDic.update({ path[0]: path[1] })
            else:
                pathDic[path[0]] = path[1]
            
            if path[1] not in pathDic:
                pathDic[path[1]] = ""
        ans = ''
        for key, value in pathDic.items():
            if value == '':
                ans = key
                break
        return ans

if __name__ == '__main__':
    #paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    paths = [["B","C"],["D","B"],["C","A"]]
    #paths = [["A","Z"]]

    sol = Solution()
    print(sol.destCity(paths))
    