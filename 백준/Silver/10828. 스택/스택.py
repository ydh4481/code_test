import sys
from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.stack else -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 0 if self.stack else 1

    def top(self):
        return self.stack[-1] if self.stack else -1


if __name__ == '__main__':
    input = sys.stdin.readline
    
    n = int(input())
    stack = Stack()

    for _ in range(n):
        line = input().split()

        if line[0] == 'push':
            stack.push(line[1])

        else:
            print(getattr(stack, line[0])())


