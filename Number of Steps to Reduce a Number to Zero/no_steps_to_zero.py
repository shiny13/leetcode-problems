import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    num = int(input.rstrip())
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1    
        steps += 1
    print(steps)
    #return steps