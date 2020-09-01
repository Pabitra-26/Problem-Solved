# Problem name: Maximum Frequency Stack
# Description: Implement FreqStack, a class which simulates the operation of a stack-like data structure.
# FreqStack has two functions:
# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the stack.
# If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


class FreqStack:

    def __init__(self):
        self.stack = []
        self.table = {}

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x in self.table:
            self.table[x] += 1
        else:
            self.table[x] = 1

    def pop(self) -> int:
        max_ele = max(list(self.table.values()))
        for i in range(len(self.stack) - 1, -1, -1):
            if (self.table[self.stack[i]] == max_ele):
                self.table[self.stack[i]] -= 1
                return self.stack.pop(i)
