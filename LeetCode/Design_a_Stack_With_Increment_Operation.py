# Problem name: Design a Stack With Increment Operation
# Description: Design a stack which supports the following operations.
# Implement the CustomStack class:
# CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
# void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
# int pop() Pops and returns the top of stack or -1 if the stack is empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []

        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if (len(self.stack) < self.maxSize):
            self.stack.append(x)

    def pop(self) -> int:
        if (self.stack == []):
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if (len(self.stack) < k):
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val

