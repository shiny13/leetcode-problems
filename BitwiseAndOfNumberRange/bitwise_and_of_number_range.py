import sys 

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while(m < n): 
            # -b is the 2's complement of b  
            # when do bitwise or with b we 
            # get LSB and we subtract that from b  
            n -= (n & -n)  
            print(n)
        return n

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    m = data[0]
    n = data[1]

    sol = Solution()
    print(sol.rangeBitwiseAnd(m,n))