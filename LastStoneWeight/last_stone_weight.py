import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    stones = list(map(int, input.split()))
    stones.sort(reverse=True)
    i = 0
    length = len(stones)
    while i+1 < length:
        x = stones[i]
        y = stones[i+1]
        if x == y:
            stones.pop(i)
            stones.pop(i)
            length-=2
        else:
            _new = x-y
            stones[i]=_new
            stones.pop(i+1)
            length-=1
            stones.sort(reverse=True)
    print(stones[0] if len(stones) == 1 else 0)
    #return stones
