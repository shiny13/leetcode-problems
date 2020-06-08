import sys 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powerOfTwo = False

        while n > 0:
            if n == 1:
                powerOfTwo = True
                break 
            
            if n % 2 == 1:
                break 
            elif n % 2 == 0:
                n = n/2

        return powerOfTwo

if __name__ == '__main__':
    input = sys.stdin.read()
    num = int(input)

    sol = Solution()
    print(sol.isPowerOfTwo(num))

