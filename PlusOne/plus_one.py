import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    digits = list(map(int, input.split()))

    multiplier = 1
    index = len(digits)-1 
    num = 0
    while index >= 0:
        num += digits[index] * multiplier
        multiplier = multiplier * 10
        index -= 1
    num+=1
    digits = [int(x) for x in str(num)]
    print(digits)
    #return digits