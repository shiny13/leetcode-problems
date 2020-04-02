import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    s = input.strip()
    arr = s.split()
    for i in range(len(arr)):
        arr[i] = arr[i] [::-1]
    newStr = ""
    newStr = " ".join(arr)
    print(newStr)
