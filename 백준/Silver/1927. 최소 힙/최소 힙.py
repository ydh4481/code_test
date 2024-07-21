import heapq
import sys


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, x)

    def pop(self):
        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)


if __name__ == '__main__':
    input = sys.stdin.readline

    min_heap = MinHeap()

    n = int(input())

    for _ in range(n):
        x = int(input())

        if x:
            min_heap.push(x)
        else:
            if len(min_heap) > 0:
                print(min_heap.pop())
            else:
                print(0)
