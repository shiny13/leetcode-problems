import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    x = data[0]
    y = data[1]
    xor = x^y
    #print("x: " + str(x) + " y: " + str(y) + " x^y: "+ str(xor))
    _xor = "{:032b}".format(xor)
    counter = 0
    for s in _xor:
        if s == "1":
            counter += 1
    print(counter)
    #return counter
