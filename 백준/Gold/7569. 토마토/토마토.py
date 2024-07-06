from collections import deque
from typing import List


def bfs(graph: List, queue: deque) -> deque:
    next_node = deque()
    while queue:
        start_node = queue.popleft()
        h, x, y = start_node
        for dx, dy, dh in [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]:
            nx, ny, nh = x + dx, y + dy, h + dh
            if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph[0][0]) and 0 <= nh < len(graph):
                if graph[nh][nx][ny] == 0:
                    graph[nh][nx][ny] = 1
                    next_node.append((nh, nx, ny))

    return next_node


def check_ripe(graph):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return False
    return True


if __name__ == '__main__':
    m, n, h = map(int, input().split())

    graph = []

    for i in range(h):
        height = []
        for j in range(n):
            height.append(list(map(int, input().split())))
        graph.append(height)
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))

    days = 0
    while queue:
        days += 1
        queue = bfs(graph, queue)

    days = days - 1 if check_ripe(graph) else -1
    print(days)
