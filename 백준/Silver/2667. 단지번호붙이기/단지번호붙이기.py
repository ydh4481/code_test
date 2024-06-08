from collections import deque


def bfs(graph, start):
    queue = deque([start])
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_, y_ = x + dx, y + dy
            if 0 <= x_ < len(graph) and 0 <= y_ < len(graph):
                if graph[x_][y_] == 1:
                    graph[x_][y_] = 0
                    queue.append((x_, y_))
                    count += 1

    return count


if __name__ == '__main__':
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, list(input()))))

    result = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                graph[i][j] = 0
                result.append(bfs(graph, (i, j)))

    print(len(result))
    for _ in sorted(result):
        print(_)
