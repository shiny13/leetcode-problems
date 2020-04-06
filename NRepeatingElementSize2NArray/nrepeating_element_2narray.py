import sys 
from queue import PriorityQueue

if __name__ == '__main__':
    input = sys.stdin.read()
    A = list(map(int, input.split()))

    n = len(A) // 2
    elements = {}
    answer = -1
    for i in A:
        item = 1
        if i not in elements:
            elements[i] = item
        else:
            item = elements.get(i)
            item+=1
            elements.update({ i: item })
        if item == n:
            answer = i 
            break
        print(elements)
    print(answer)
    #return answer