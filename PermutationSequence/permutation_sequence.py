import sys 

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        num = [1]
        i=1
        while(i < n):
            num.append(i+1)
            a  = fact.pop(len(fact)-1)
            fact.append(a)
            fact.append(a*i)
            i+=1
        print(fact)
        print(num)
        i=1
        str_n = 0
        k-=1
        while(i <= n):
            index = int((k)/fact[n-i])
            str_n = 10*str_n + num[index]
            num.remove(num[index])
            k %=fact[n-i]
            i+=1
        return str(str_n)

if __name__ == '__main__':
    input = sys.stdin.read().strip()
    data = list(map(int, input.split()))

    sol = Solution()
    print(sol.getPermutation(data[0], data[1]))