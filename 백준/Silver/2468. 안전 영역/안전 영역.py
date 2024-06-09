import sys
from collections import deque


def bfs(graph, start_node, target_height, visited):
    queue = deque([start_node])
    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                if graph[nx][ny] >= target_height and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    return visited


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    graph = []

    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    max_h = max([max(_) for _ in graph])

    answer = 0
    for target_h in range(max_h, 0, -1):
        visited_nodes = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 0
        for x in range(n):
            for y in range(n):
                if graph[x][y] >= target_h and not visited_nodes[x][y]:
                    cnt += 1
                    bfs(graph, (x, y), target_h, visited_nodes)
        answer = max(answer, cnt)
    print(answer)
