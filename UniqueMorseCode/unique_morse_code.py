import sys
if __name__ == '__main__':
    input = sys.stdin.read()
    words = input.strip().split()
    #morse codes
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
                 ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
                 ".--","-..-","-.--","--.."]
    morse_map = {}
    dec = 97
    for i in range(len(morse)):
        morse_map[chr(dec)] = morse[i]
        dec += 1
    coded = {}
    for word in words:
        _coded = ""
        for i in range(len(word)):
            _coded += morse_map.get(word[i])
        if _coded not in coded:
            coded[_coded] = 1
        #else:
        # Good to have but not needed in this problem
        #    coded.update({ _coded: coded.get(_coded)+1})
    
    print(coded)
    print(len(coded))
    #return len(coded)