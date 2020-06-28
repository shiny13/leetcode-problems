import sys 
from typing import List 
from collections import defaultdict

class Solution:
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        output = []
        outputDic = {}
        searchItem = 'JFK'
        while len(tickets) > 0:
            for i in range(len(tickets)):
                if tickets[i][0] != searchItem:
                    continue 
                if tickets[i][0] == searchItem:
                    if tickets[i][0] not in outputDic:
                        outputDic[tickets[i][0]] = [tickets[i][1]]
                    elif tickets[i][0] in outputDic:
                        item = outputDic.get(tickets[i][0])
                        item.append(tickets[i][1])
                        item.sort()
                        outputDic.update({ tickets[i][0]: item })

                    searchItem = tickets[i][1]
                    tickets.pop(i)
                    break 
        
        searchItem = 'JFK'
        while len(outputDic) > 0:
            item = outputDic.get(searchItem)
            for val in item:
                output.append(searchItem)
                output.append(val)
            del outputDic[searchItem]
            searchItem = output[-1]
        return output
        """

    # Better DFS solution
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.route = []
        self.adj_list = defaultdict(list)
        for i,j in tickets:
            self.adj_list[i].append(j)
        for key in self.adj_list: 
            self.adj_list[key] = sorted(self.adj_list[key], reverse=True)
            
        self.dfs("JFK")
        return self.route[::-1]
    
    def dfs(self, airport):
        while self.adj_list[airport]:
            candidate = self.adj_list[airport].pop()
            self.dfs(candidate)
        self.route.append(airport)

if __name__ == '__main__':
    Input = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    #Input = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

    sol = Solution() 
    print(sol.findItinerary(Input))
