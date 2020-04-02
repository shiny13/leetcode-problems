import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    A = list(map(int, input.split()))

    i = 0
    odd = []
    while i < len(A):
        if A[i] % 2 != 0:
            temp = A[i]
            A.pop(i)
            i -= 1
            odd.append(temp)
        i += 1
    A = A + odd
    print(A)
    #return A