import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    n = nums[0]

    digits = []
    #extract digits
    if n < 10:
        digits.append(n)
    while n > 9:
        digits.insert(0,n%10)
        n = int(n//10)
        #print(n)
        if n < 10:
            digits.insert(0,n)
    #print(digits)

    _product = 1
    _sum = 0
    for d in digits:
        _product *= d
        _sum += d 
    print(_product - _sum)
    #return _product - _sum