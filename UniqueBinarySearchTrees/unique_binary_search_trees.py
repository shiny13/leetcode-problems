import sys 

class Solution:
    def numTrees(self, n: int) -> int:
        #Catalan solution
        numTree = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]

if __name__ == '__main__':
    input = sys.stdin.read().strip()
    data = int(input)

    sol = Solution()
    print(sol.numTrees(data))
