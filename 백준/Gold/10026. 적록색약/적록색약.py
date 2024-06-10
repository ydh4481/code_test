import sys
sys.setrecursionlimit(10 ** 5)


def dfs(graph, start, target):
    graph[start[0]][start[1]] = 1

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = start[0] + dx, start[1] + dy
        if 0 <= nx < len(graph) and 0 <= ny < len(graph):
            if graph[nx][ny] == target:
                dfs(graph, (nx, ny), target)


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    graph = []
    bn_graph = []
    for _ in range(n):
        row = sys.stdin.readline()
        graph.append(list(row)[:-1])
        bn_graph.append(list(row.replace('R', 'G'))[:-1])

    cnt = 0
    bn_cnt = 0
    for x in range(n):
        for y in range(n):
            target = graph[x][y]
            if target != 1:
                cnt += 1
                dfs(graph, (x, y), target)

    for x in range(n):
        for y in range(n):
            bn_target = bn_graph[x][y]
            if bn_target != 1:
                bn_cnt += 1
                dfs(bn_graph, (x, y), bn_target)

    print(cnt, bn_cnt)
