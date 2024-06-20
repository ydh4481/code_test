from collections import deque


def bfs(graph, target):
    queue = deque([(0, 0, 0)])
    visited = [[[0] * 2 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    visited[0][0][0] = 1

    while queue:
        x, y, w = queue.popleft()

        if (x, y) == target:
            return visited[x][y][w]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 1 and w == 0:  # 현재 위치 벽, 아직 벽 부수지 않았다면
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

                elif graph[nx][ny] == 0 and not visited[nx][ny][w]:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append((nx, ny, w))
    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = []

    for _ in range(n):
        graph.append(list(map(int, list(input()))))

    print(bfs(graph, (n - 1, m - 1)))
