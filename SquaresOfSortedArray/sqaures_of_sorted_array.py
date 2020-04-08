import sys 
import heapq

if __name__ == '__main__':
    input = sys.stdin.read()
    A = list(map(int, input.split()))

    output = []
    for value in A:
        sq = value * value 
        heapq.heappush(output, sq)
    
    print([heapq.heappop(output) for i in range(len(output))])
    #return [heapq.heappop(output) for i in range(len(output))]