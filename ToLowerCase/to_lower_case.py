import sys
if __name__ == '__main__':
    input = sys.stdin.read()
    _str = str(input.strip())

    _newStr = ""
    for i in range(len(_str)):
        if ord(_str[i]) >= 65 and ord(_str[i]) <= 90:
            _newStr += str(chr(ord(_str[i]) + 32))
        else:
            _newStr += _str[i]
    print(_newStr)
