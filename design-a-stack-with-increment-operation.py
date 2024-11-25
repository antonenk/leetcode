#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 20% runtime / 35% mem


class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        
    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1
        
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


def test_1():
    stk = CustomStack(3)
    stk.push(1)                           # stack becomes [1]
    stk.push(2)                           # stack becomes [1, 2]
    assert stk.pop() == 2                 # return 2 --> Return top of the stack 2, stack becomes [1]
    stk.push(2)                           # stack becomes [1, 2]
    stk.push(3)                           # stack becomes [1, 2, 3]
    stk.push(4)                           # stack still [1, 2, 3], Do not add another elements as size is 4
    stk.increment(5, 100);                # stack becomes [101, 102, 103]
    stk.increment(2, 100);                # stack becomes [201, 202, 103]
    assert stk.pop() == 103               # return 103 --> Return top of the stack 103, stack becomes [201, 202]
    assert stk.pop() == 202               # return 202 --> Return top of the stack 202, stack becomes [201]
    assert stk.pop() == 201               # return 201 --> Return top of the stack 201, stack becomes []
    assert stk.pop() == -1                # return -1 --> Stack is empty return -1.


if __name__ == '__main__':
    test_1()
