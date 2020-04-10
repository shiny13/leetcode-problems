
"""
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        return 0
"""
if __name__ == '__main__':
    # Test input
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    length = len(grid)
    vertical = [-1] * length
    horizontal = [-1] * length

    for i in range(length):
        for j in range(length): 
            vertical[i] = max(vertical[i], grid[j][i])
            horizontal[i] = max(horizontal[i], grid[i][j])
    #print(vertical)
    #print(horizontal)
    increase = 0
    for i in range(length):
        for j in range(length): 
            max_vertical = vertical[j]
            max_horizontal = horizontal[i]
            max_increase = min(max_vertical, max_horizontal)
            #print(max_increase)
            increase += max_increase - grid[i][j]
            grid[i][j] += max_increase - grid[i][j]
    
    print(grid)
    print("increase: " + str(increase))
    #return increase