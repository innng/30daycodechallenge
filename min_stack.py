class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.tail = []

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = x
        else:
            self.tail.append(self.head)
            self.head = x

    def pop(self) -> None:
        if len(self.tail) > 0:
            self.head = self.tail.pop(-1)
        else:
            self.head = None

    def top(self) -> int:
        return self.head

    def getMin(self) -> int:
        return min([self.head] + self.tail)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
