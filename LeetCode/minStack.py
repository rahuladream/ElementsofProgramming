"""


"""



class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self):
        return min(self.stack)


if __name__ == "__main__":
    minStack = MinStack();
    minStack.push(-2)
    minStack.push(0);
    minStack.push(-3);
    print(minStack.getMin())   
    minStack.pop();
    print(minStack.top())
    print(minStack.getMin())   