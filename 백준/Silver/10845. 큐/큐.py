import sys
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.popleft() if self.queue else -1

    def size(self):
        return len(self.queue)

    def empty(self):
        return 0 if self.queue else 1

    def front(self):
        return self.queue[0] if self.queue else -1

    def back(self):
        return self.queue[-1] if self.queue else -1


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    queue = Queue()

    for _ in range(n):
        line = input().split()

        if line[0] == 'push':
            queue.push(line[1])

        else:
            print(getattr(queue, line[0])())
