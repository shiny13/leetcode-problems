import sys

if __name__ == '__main__':
    #input = sys.stdin.read()
    #A = list(map(int, input.split()))

    #sample input
    #costs = [[10,20],[30,200],[400,50],[30,20]]
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

    # sort the list based on diffrence
    costs.sort(key = lambda x : (x[0]-x[1]))
        
    #send first n//2 to city. A
    # last n//2 to city B
    n=len(costs)
    print(costs)
        
    to_city_A = sum ( [ costs[i][0] for i in range(n//2) ] )
    to_city_B = sum ( [ costs[i][1] for i in range(n//2,n)] )
        
    print(to_city_A,to_city_B)
    #return (to_city_A+to_city_B)