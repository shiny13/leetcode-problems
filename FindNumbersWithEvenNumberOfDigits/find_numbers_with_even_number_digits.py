import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))

    output = 0
    for n in nums:
        digits = 0
        if n < 10:
            digits += 1
        while n > 9:            
            n = int(n//10)
            digits += 1
            if n < 10:
                digits += 1
        if digits % 2 == 0:
            output+=1
    print(output)
    #return output
