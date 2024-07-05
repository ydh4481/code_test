import copy
from collections import deque
from itertools import combinations


def bfs(graph, queue):
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))

    return graph


if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    virus_nodes = deque()
    wall_nodes = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 2:
                virus_nodes.append((x, y))
            if graph[x][y] == 0:
                wall_nodes.append((x, y))

    answer = 0
    for combi in combinations([i for i in range(len(wall_nodes))], 3):
        new_graph = copy.deepcopy(graph)
        new_virus_nodes = copy.deepcopy(virus_nodes)
        for idx in combi:
            x, y = wall_nodes[idx]
            new_graph[x][y] = 1

        new_graph = bfs(new_graph, new_virus_nodes)
        safe_area = 0
        for row in new_graph:
            for val in row:
                if val == 0:
                    safe_area += 1
        answer = max(answer, safe_area)

    print(answer)
