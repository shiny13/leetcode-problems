import sys 
import random 

class Codec:
    def __init__(self):
        self.shortLong = {}

    def encode(self, longUrl: str) -> str:
        chars = [chr(d) for d in range(ord('0'), ord('9')+1)]
        chars.extend([chr(d) for d in range(ord('A'), ord('Z')+1)])
        chars.extend([chr(d) for d in range(ord('a'), ord('z')+1)])
        print(chars)
        def getRandomChars(length):
            _ans = ''
            for i in range(length):
                _ans += chars[random.randrange(0,61)]
            return _ans 

        length = 6
        ans = getRandomChars(length)
        if ans in self.shortLong and longUrl != self.shortLong.get(ans):
            while ans in self.shortLong:
                ans = getRandomChars(length)

        self.shortLong[ans] = longUrl

        return "http://tinyurl.com/"+ans
        

    def decode(self, shortUrl: str) -> str:
        last = shortUrl.split("/")[-1]
        return self.shortLong[last]

if __name__ == '__main__':
    input = sys.stdin.read()
    _url = input.strip()

    codec = Codec()
    _tinyUrl = codec.encode(_url)
    print(_tinyUrl)
    _decodedUrl = codec.decode(_tinyUrl)
    print(_decodedUrl)
