import sys 
from typing import List
import heapq
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], 
    src: int, dst: int, K: int) -> int:

        graph = collections.defaultdict(list)
        deque_vert = collections.deque([[src, 0, 0]])
        min_price = float('inf')
    
        for i, j, k in flights: 
            graph[i].append([j, k])

        while deque_vert:
            city, visited, price = deque_vert.popleft()

            if price <= min_price and visited <= K and city != dst:
                for neibh, price_neibh in graph[city]:
                     deque_vert.append([neibh, visited + 1, price + price_neibh])
            
            if city == dst:
                min_price = min(min_price, price)
        
        return min_price if min_price != float('inf') else -1

if __name__ == '__main__':
    n = 3
    edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1

    sol = Solution()
    print(sol.findCheapestPrice(n, edges, src, dst, k))