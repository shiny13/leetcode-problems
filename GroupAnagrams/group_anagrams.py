import sys 

if __name__ == '__main__':
    input = sys.stdin.read()
    strs = input.split()

    _map = {}
    for val in strs:
        a_val = ord('a')
        _chars = [0] * 26 
        for v in val:
            _chars[ord(v) - a_val] += 1
        chars = ""
        for i, c in enumerate(_chars):
            chars += str(c)
        print(chars)
        if chars in _map:
            arr = _map.get(chars, [])
            arr.append(val)
            _map.update({ chars: arr })
        else:
            _map[chars] = [val]
    answer = []
    for key in _map:
        answer.append(_map[key])
    print(answer)
    #return answer
