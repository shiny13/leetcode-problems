import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    S = input.strip()
    length = len(S)
    i = 0
    output = []
    for s in S:
        if s == "I":
            output.append(i)
            i+=1
        else:
            output.append(length)
            length-=1
    output.append(length)
    print(output)
    #return output