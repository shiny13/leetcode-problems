import sys 

class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows, next = 0, 1
        while n >= next:
            rows += 1 
            n -= next 
            next += 1

        return rows

if __name__ == '__main__':
    input = int(sys.stdin.read().strip())

    sol = Solution()
    print(sol.arrangeCoins(input))
