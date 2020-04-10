import sys 

def _helper(s):
        while "#" in s:
            i = s.index("#")
            s = s[:i-1] + s[i+1:] if i > 0 else s[i+1:]
        return s

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    S = data[0]
    T = data[1]

    S, T = _helper(S), _helper(T)
    print(S == T)
    #return S == T