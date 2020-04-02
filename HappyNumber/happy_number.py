import sys

def digit_square(num):
        base = 1
        result = 0
        while num % base < num:
            digit = num // base % 10
            result += digit * digit
            base *= 10
        return result

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input.strip())

    """
    walker = n
        runner = self.digit_square(n)

        while runner != walker:
            runner = self.digit_square(runner)
            runner = self.digit_square(runner)
            walker = self.digit_square(walker)

        return walker == 1
    """

    occurrence_set = set()
    current = n
    while current != 1:
        current = digit_square(current)
        if current in occurrence_set: 
            #return False
            print(False)
        occurrence_set.add(current)

    #return True
    print(True)