from collections import deque


def bfs(graph, start):
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))


if __name__ == '__main__':
    t = int(input())

    for t_ in range(t):
        m, n, k = map(int, input().split())

        graph = [[0 for _ in range(n)] for _ in range(m)]
        for _ in range(k):
            x, y = map(int, input().split())
            graph[x][y] = 1
        cnt = 0
        for y in range(n):
            for x in range(m):
                if graph[x][y] == 1:
                    cnt += 1
                    graph[x][y] = 0
                    bfs(graph, (x, y))
        print(cnt)
