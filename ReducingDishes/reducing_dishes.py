import sys 
from typing import List

class Solution:
    #not the correct answer :(
    """
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        mult = 1
        maxSat = 0
        zeroOrPositiveIndex = -1
        zeroOrPositiveIdxFound = False
        cumSum = 0

        for i, val in enumerate(satisfaction):
            if not zeroOrPositiveIdxFound and satisfaction[i] > 0:
                zeroOrPositiveIndex = i-1
                zeroOrPositiveIdxFound = True 
            if satisfaction[i] < 0:
                continue
            maxSat += satisfaction[i] * mult 
            mult += 1
            cumSum += satisfaction[i]

        while zeroOrPositiveIndex >= 0:
            curSat = satisfaction[zeroOrPositiveIndex] + maxSat + cumSum
            if curSat > maxSat:
                maxSat = curSat
            cumSum += satisfaction[zeroOrPositiveIndex]
            zeroOrPositiveIndex -= 1

        return maxSat 
    """
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        s=sorted(satisfaction)
        if s[-1]<=0:
            return 0
        # Calculate score while popping elements from sorted array. 
		# Once the score drops, return the maximum.
        s1=s2=0
        while len(s)>0:
            s1=sum((i+1)*n for i,n in enumerate(s))
            s.pop(0)
            if s1>0:
                if s2==0:
                    s2=s1
                elif s2>s1:
                    return s2
                else:
                    s2=s1
        return s1

if __name__ == '__main__':
    input = sys.stdin.read()
    satisfaction = list(map(int, input.split()))

    sol = Solution()
    print(sol.maxSatisfaction(satisfaction))
