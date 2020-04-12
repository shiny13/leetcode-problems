import sys 

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

if __name__ == '__main__':
    input = sys.stdin.read()
    stones = list(map(int, input.split()))
    stones.sort(reverse=True)
    #print(stones)
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
