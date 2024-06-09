import sys
from collections import deque


def D(x):
    return x * 2 % 10000


def S(x):
    return x - 1 if x else 9999


def L(x):
    return x // 1000 + (x % 1000) * 10


def R(x):
    return x // 10 + (x % 10) * 1000


def bfs(start, end):
    graph = [0] * 10001

    queue = deque([(start, '')])

    while queue:
        curr_val, command = queue.popleft()
        if curr_val == end:
            return command
        for func in [D, S, L, R]:
            next_val = func(curr_val)
            if not graph[next_val]:
                graph[next_val] = 1
                queue.append((next_val, command + func.__name__))


if __name__ == '__main__':
    t = int(sys.stdin.readline())

    for test_case in range(t):
        start, end = map(int, sys.stdin.readline().split())

        print(bfs(start, end))

# TEST CASE
"""
1
1234 3412

1
0 1000

SDDLDSLDRDDD
"""
