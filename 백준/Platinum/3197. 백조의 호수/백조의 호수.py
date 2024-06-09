import sys
from collections import deque


def melt(graph, queue):
    next_queue = deque()

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 'X':
                    graph[nx][ny] = '.'
                    next_queue.append((nx, ny))

    return next_queue


def bfs(graph, queue, end, visited):
    next_queue = deque()
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True, None
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if not visited[nx][ny]:
                    if graph[nx][ny] == 'X':
                        next_queue.append((nx, ny))
                    else:
                        queue.append((nx, ny))
                    visited[nx][ny] = 1

    return False, next_queue


if __name__ == '__main__':
    r, c = map(int, sys.stdin.readline().split())
    graph = []

    for _ in range(r):
        graph.append(list(sys.stdin.readline())[:-1])

    swans = []
    days = 0
    ice_queue = deque()
    for x in range(r):
        for y in range(c):
            if graph[x][y] in ('.', 'L'):
                ice_queue.append((x, y))
            if graph[x][y] == 'L':
                swans.append((x, y))

    swan_queue = deque([swans[0]])
    swan_visited = [[0 for _ in range(c)] for _ in range(r)]
    swan_visited[swans[0][0]][swans[0][1]] = 1

    while True:
        ck, swan_queue = bfs(graph, swan_queue, swans[1], swan_visited)
        if ck: break

        days += 1
        ice_queue = melt(graph, ice_queue)

    print(days)
