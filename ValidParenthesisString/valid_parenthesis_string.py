import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    s = input.strip()

    # balance of left parenthesis and right parenthesis
    leftBalance = rightBalance = 0
    n = len(s)
    output = True
    for i in range(n):
        if s[i] in "(*":
            leftBalance += 1
        else:
            leftBalance -= 1
        
        if s[n-i-1] in "*)":
            rightBalance += 1
        else:
            rightBalance -= 1
        if leftBalance < 0  or rightBalance < 0:
            #return False
            output = False
    print(output)
    #return True
