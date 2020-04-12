import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    A = list(map(int, input.split()))
    output = 0
    for i in range(len(A)):
        print(str(A[i]) + " " + str(A[i+1]))
        if A[i] > A[i+1]:
            output = i
            break
    print(output)