import math
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = math.inf        

    def push(self, x: int) -> None:
        self.stack.append(x)
        for i in self.stack:
            if i < self.min:
                self.min = i
                print("new min: " + str(self.min))

    def pop(self) -> None:
        popped = self.stack[len(self.stack)-1]
        self.stack.pop(len(self.stack)-1)
        if len(self.stack) == 0:
            self.min = math.inf
        else:
            if popped == self.min:
                self.min = math.inf
            print("len after pop: " + str(len(self.stack)))
            for i in self.stack:
                if i < self.min:
                    self.min = i
                    print("new min: " + str(self.min))

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min

if __name__ == '__main__':
# Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.stack)
    #print("len: " + str(len(obj.stack)))
    print(obj.getMin())
    obj.pop() 
    print(obj.top())
    print(obj.getMin())