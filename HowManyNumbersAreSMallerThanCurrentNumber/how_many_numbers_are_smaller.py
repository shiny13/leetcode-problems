import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))

    print([len(list(filter(lambda x: x<i,nums))) for i in nums])
    #return [len(list(filter(lambda x: x<i,nums))) for i in nums]