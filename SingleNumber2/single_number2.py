import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    print(data)
    items = {}
    for i in range(len(data)):
        if data[i] not in items:
            items[data[i]] = 1
        elif data[i] in items and items[data[i]] == 2:
            items.pop(data[i], None)
        elif data[i] in items:
            items.update({ data[i]: 2 })
    print(list(items.keys())[0])
    
