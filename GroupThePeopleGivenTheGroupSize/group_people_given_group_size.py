import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    groupSizes = list(map(int, input.split()))

    groupMap = {}
    for i, g in enumerate(groupSizes):
        if g not in groupMap:
            groupMap[g] = [[i]]
        else: 
            values = groupMap.get(g)
            val = values[len(values)-1]
            if len(val) == g:
                values.append([i])
            else:
                val.append(i)
                values[len(values)-1] = val 
            groupMap.update({ g: values })
    output = []
    for key in groupMap:
        output = output + groupMap.get(key)
    print(output)
    #return output