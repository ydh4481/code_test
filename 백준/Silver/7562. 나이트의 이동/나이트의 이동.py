import sys
from collections import deque


def bfs(l, start, end):
    queue = deque([start])
    visited = [[0 for _ in range(l)] for _ in range(l)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return visited[x][y]

        for dx, dy in [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


if __name__ == '__main__':
    t = int(sys.stdin.readline())

    for test_case in range(t):
        l = int(sys.stdin.readline())
        curr_x, curr_y = map(int, sys.stdin.readline().split())
        end_x, end_y = map(int, sys.stdin.readline().split())

        answer = bfs(l, (curr_x, curr_y), (end_x, end_y))
        print(answer)
