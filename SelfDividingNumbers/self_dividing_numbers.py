import sys 

def self_dividing(n):
        for d in str(n):
            if d == '0' or n % int(d) > 0:
                return False
        return True

if __name__ == '__main__':
    input = sys.stdin.read()
    bound = list(map(int, input.split()))
    left = bound[0]
    right = bound[1]

    """
    output = []
    for i in range(left, right+1):
        if i < 10:
            output.append(i)
            continue
        res = set(map(int, str(i)))
        add = -1
        for r in res:
            if r == 0:
                break 
            if i % r == 0:
                add = 0
            else:
                add = -1
                break        
        if add == -1:
            continue
        output.append(i)
    print(output)
    #return output
    """

    ans = []
    for n in range(left, right + 1):
        if self_dividing(n):
            ans.append(n)
    print(ans)
    #return ans