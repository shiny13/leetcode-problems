import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))

    """
    output = list(nums)
    print(output)
    total = 1
    for i in range(len(nums)):
        total = total * nums[i]
    for i in range(len(output)):
        output[i] = int(total / output[i])
    """
    output = []
    left = [1 for _ in nums]
    right = [1 for _ in nums]
    for i in range(len(nums)-1):
        right[i+1] = right[i] * nums[i]
    #print(right)
    i = len(nums)-1
    while i > 0:
        left[i-1] = left[i] * nums[i]
        i-=1 
    #print(left)
    for i in range(len(left)):
        output.append(left[i] * right[i])

    print(output)
    #return output

    ## Best solution
    # The length of the input array 
    length = len(nums)
    # The answer array to be returned
    answer = [0]*length
        
    # answer[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the answer[0] would be 1
    answer[0] = 1
    for i in range(1, length):        
        # answer[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with nums[i - 1] would give the product of all 
        # elements to the left of index 'i'
        answer[i] = nums[i - 1] * answer[i - 1]
        
    # R contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R would be 1
    R = 1
    for i in reversed(range(length)):   
        # For the index 'i', R would contain the 
        # product of all elements to the right. We update R accordingly
        answer[i] = answer[i] * R
        R *= nums[i]
    print(answer)    
    #return answer
