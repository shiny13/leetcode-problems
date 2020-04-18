import sys
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        islands = {}
        data = []
        visited = []
        for i in range(len(grid)):
            data.append([])
            visited.append([])
            for s in grid[i]:
                data[i].append(int(s))
                visited[i].append(False)

        ## more logic goes here
        for y in range(len(data)):
            for x in range(len(data[y])):
                self.traverse(data,visited,islands,x,y) 
        print(islands)
        print(len(islands))
        return len(islands)

    def checkIsland(self, islands, x, y)->int:
        result = 1
        if len(islands) == 0:
            return result

        point = "{},{}".format(y,x)
        left = "{},{}".format(y,x-1)
        above = "{},{}".format(y-1,x)
        right = "{},{}".format(y,x+1)
        below = "{},{}".format(y+1,x)
        found = False
        for key in islands:
            value = islands.get(key)
            if point in value:
                found = True
                result = key
                break
            if left in value or above in value or right in value or below in value:
                value = islands.get(key)
                value += "-"+point
                islands.update({ key: value })
                found = True
                result = key
                break

        if not found:
            result = len(islands) + 1 
        return result

    def traverse(self, data, visited, islands, x, y):
        if visited[y][x]:
            return
        visited[y][x] = True
        if data[y][x] == 0:
            return
        island = self.checkIsland(islands, x, y)
        if island not in islands:
            islands[island] = "{},{}".format(y,x)
        
        #Look left for land
        if x-1 >= 0: 
            self.traverse(data, visited, islands, x-1, y)
        #Look above for land
        if y-1 >= 0: 
            self.traverse(data, visited, islands, x, y-1)
        #Look right for land 
        if x+1 < len(data[y]):
            self.traverse(data, visited, islands, x+1, y)
        #Look below for land
        if y+1 < len(data):
            self.traverse(data, visited, islands, x, y+1)

if __name__ == '__main__':
    input = sys.stdin.read()
    grid = list(input.split())
    sol = Solution()
    sol.numIslands(grid)

