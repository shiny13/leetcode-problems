import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    
    m = max(nums)
    if all(m >= 2*x for x in nums if x != m):
        #return nums.index(m)
        print(nums.index(m))
    #return -1
    print(-1)