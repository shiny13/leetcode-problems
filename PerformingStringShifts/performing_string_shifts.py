import sys

if __name__ == '__main__':
    # sample input
    s = "abc" 
    shift = [[0,1], [1,2]]
    #s = "abcdefg"
    #shift = [[1,1],[1,1],[0,2],[1,3]]
    #s = "wpdhhcj"
    #shift = [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]
    #s = "xqgwkiqpif"
    #shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]

    _new = s
    for item in shift:
        if item[0] == 0:
            _lshift = item[1]
            _new = _new[_lshift:] + _new[0: _lshift] 
            print(_new)
        elif item[0] == 1:
            _rshift = item[1]
            _new = _new[len(s) - _rshift:] + _new[0:len(s) - _rshift] 
            print(_new)
    print(_new)
    #return _new 
