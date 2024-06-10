import sys


def dfs(graph, start_node):
    graph[start_node[0]][start_node[1]] = 0

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        nx, ny = start_node[0] + dx, start_node[1] + dy
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if graph[nx][ny] == 1:
                dfs(graph, (nx, ny))


if __name__ == '__main__':
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == 0 and h == 0: break

        graph = []
        for _ in range(h):
            graph.append(list(map(int, sys.stdin.readline().split())))

        answer = 0
        for x in range(h):
            for y in range(w):
                if graph[x][y] == 1:
                    answer += 1
                    dfs(graph, (x, y))
        print(answer)
