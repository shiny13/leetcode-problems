import sys 

if __name__ == '__main__':
    moves = sys.stdin.read()
    #nums = list(map(int, input.split()))
    _moves = { "U": 0, "D": 0, "L": 0, "R": 0 }
    for i in moves:
        val = _moves.get(i, 0)
        _moves.update({ i: val+1 })
    
    if _moves.get("U") == _moves.get("D") and _moves.get("L") == _moves.get("R"):
        print(True)
        #return True
    else:
        print(False)
        #return False