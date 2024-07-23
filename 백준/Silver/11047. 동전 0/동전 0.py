import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())

    w = deque()
    for _ in range(n):
        w.appendleft(int(input()))
    cnt = 0
    while k:
        money = w.popleft()
        cnt += k // money
        k %= money
    
    print(cnt)
