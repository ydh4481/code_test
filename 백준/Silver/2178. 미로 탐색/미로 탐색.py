from collections import deque


def bfs(graph, start, end):
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if (x, y) == end: break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x_, y_ = x + dx, y + dy
            if 0 <= x_ < len(graph) and 0 <= y_ < len(graph[0]):
                if graph[x_][y_] == 1:
                    queue.append((x_, y_))
                    graph[x_][y_] = graph[x][y] + 1

    return graph[end[0]][end[1]]


if __name__ == '__main__':
    n, m = map(int, input().split())

    maze = []

    for i in range(n):
        maze.append(list(map(int, list(input()))))
    print(bfs(maze, (0, 0), (n - 1, m - 1)))
