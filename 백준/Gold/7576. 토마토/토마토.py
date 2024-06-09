from collections import deque


def bfs(graph, queue):
    visited = []

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 0 and graph[nx][ny] not in visited:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))


def calculate_days(graph):
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y] == 0:
                return -1

    return max([max(_) for _ in graph]) - 1


if __name__ == '__main__':
    m, n = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    targets = deque()
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                targets.append((x, y))
    bfs(graph, targets)

    print(calculate_days(graph))
