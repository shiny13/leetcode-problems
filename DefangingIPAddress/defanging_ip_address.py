import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = str(input).rstrip()
    chars = [char for char in data] 
    #print(chars)
    i = 0
    newStr = ""
    while i < len(chars): 
        if chars[i] == '.':
            newStr += "[.]"
            #continue
        else:
            newStr += chars[i]
        i += 1
    #print(chars)
    print(newStr)
    #return newStr