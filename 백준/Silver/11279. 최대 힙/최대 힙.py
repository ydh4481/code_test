import heapq
import sys


class MaxHeap:

    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)


if __name__ == '__main__':
    n = int(input())

    max_heap = MaxHeap()

    for _ in range(n):
        x = int(sys.stdin.readline())
        if x:
            max_heap.push(x)
        else:
            if len(max_heap):
                print(max_heap.pop())
            else:
                print(0)
