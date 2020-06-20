import sys 

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        output = []
        if n == 0 or k < 0:
            return ''

        string = ''
        factorial = 1
        for i in range(1,n+1) : string += str(factorial*i) 

        def toString(_myList):
            return ''.join(_myList)

        # Permutation function for backtracking
        def permutation(_str, left, right):
            if left==right: 
                output.append(toString(_str))
            else:
                for i in range(left, right+1):
                    _str[left], _str[i] = _str[i], _str[left]
                    permutation(_str, left+1, right)
                    _str[left], _str[i] = _str[i], _str[left] #backtrack

        permutation(list(string), 0, len(string)-1)
        output.sort()
        print(output)
        return output[k-1]

if __name__ == '__main__':
    input = sys.stdin.read().strip()
    data = list(map(int, input.split()))

    sol = Solution()
    print(sol.getPermutation(data[0], data[1]))
    