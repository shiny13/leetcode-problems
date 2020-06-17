import sys 
from typing import List 

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0: return 
        rows = len(board)
        cols = len(board[0])
        #print("rows {} cols {}".format(rows,cols))
        def dfs(board: List[List[str]], i: int, j: int) -> None:
            print("rows {} cols {}".format(rows,cols))
            if i<0 or i>= rows or j<0 or j>= cols or board[i][j] != 'O':
                return 
            board[i][j] = 'E'
            dfs(board,i-1, j)
            dfs(board,i, j-1)
            dfs(board,i, j+1)
            dfs(board,i+1, j)

        #traverse all boundaries and mark all boundary Os and conencted Os as E
        for i in range(rows): 
            if board[i][0] == 'O':
                dfs(board,i,0)
            if board[i][cols-1] == 'O':
                dfs(board,i,cols-1)
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(board,0,j)
            if board[rows-1][j] == 'O':
                dfs(board,rows-1,j)
        for _r in board: print(_r)
        print('--- --- --- --- ---')
        # Traverse through the 2D array and change 
        # remaining Os to X, Es to O
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'E':
                    board[i][j] = 'O'

        #print the last array for test
        #for _r in visited: print(_r)
        for _r in board: print(_r)

if __name__ == '__main__':
    #data = sys.stdin.read().strip()

    data = [['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X'],
            ['X', 'O', 'X', 'X']]

    sol = Solution()
    sol.solve(data)