import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    prices = list(map(int, input.split()))

    i = 0
    if len(prices) == 0:
        print(maxprofit)
    valley = prices[0]
    peak = prices[0]
    maxprofit = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and (i+1)<len(prices) and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        while i < len(prices) - 1 and (i+1)<len(prices) and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]
        maxprofit += peak - valley
    print(maxprofit)
    #return maxprofit