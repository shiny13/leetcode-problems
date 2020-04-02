import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    J = data[0]
    S = data[1]
    #types = {}
    #for i in range(len(J)):
    #    types[J[i]] = 0
    #print(types)
    val=0
    for i in range(len(S)):
        #if S[i] in types:
        #    types[S[i]] = types.get(S[i]) + 1
        if S[i] in J:
            val+=1
    print(val)
    #print(sum(types.values()))
    #return val
