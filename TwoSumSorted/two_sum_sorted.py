import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    nums = data[0:len(data)-1]
    temp = data[len(data)-1:]
    target = temp[0]

    #Approach 1 using dictionary
    _hashmap = {}
    """
    for i in range(len(nums)):
        _hashmap[nums[i]] = i
    print(_hashmap)
    """
    
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in _hashmap and _hashmap[compliment] != i:
            print("Hashmap Method Answer: [" + str(i+1) + "," + str(_hashmap.get(compliment)+1) + "]")
            #return [i+1, _hashmap.get(compliment)+1]
            break
        _hashmap[nums[i]] = i