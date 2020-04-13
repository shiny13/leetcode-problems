import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    """
    _map = {0: -1}
    maxlen=0
    count=0
    for i in range(len(nums)):
        count = count + (1 if nums[i] == 1 else -1)
        if count in _map:
            print(i - _map.get(count))
            maxlen = max(maxlen, i - _map.get(count))
        else:
            _map[count] = -1
    print(_map)
    print(maxlen)
    #return maxlen
    """

    arr = []
    for i in range(2*len(nums)+2):
        arr.append(-2)
    arr[len(nums)] = -1
    maxlen=0
    count=0
    for i in range(len(nums)):
        count = count + (-1 if nums[i] == 0 else 1)
        if arr[count + len(nums)] >= -1:
            maxlen = max(maxlen, i-arr[count+len(nums)])
        else:
            arr[count+len(nums)] = i 
    print(maxlen)
    #return maxlen
