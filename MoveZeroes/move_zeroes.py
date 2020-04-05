import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))

    i = 0
    zeroes = []
    length = len(nums)
    while i < length:
        #print("i: " + str(i) + " nums["+ str(i) +"] " + str(nums[i]))
        if nums[i] == 0:
            zeroes.append(0)
            nums.pop(i)
            length -= 1
            i -= 1
        i += 1

    #nums = nums + zeroes
    for i in zeroes:
        nums.append(i)

    print(nums)
