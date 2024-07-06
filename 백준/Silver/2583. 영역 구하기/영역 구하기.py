import sys

sys.setrecursionlimit(10 ** 5)


def dfs(graph, start):
    global area
    x, y = start
    graph[x][y] = 1
    area += 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if graph[nx][ny] == 0:
                dfs(graph, (nx, ny))
    return


if __name__ == '__main__':
    m, n, k = map(int, input().split())
    graph = [[0 for j in range(m)] for i in range(n)]

    for _ in range(k):
        xy = list(map(int, input().split()))
        for x in range(xy[0], xy[2]):
            for y in range(xy[1], xy[3]):
                graph[x][y] = 1
    cnt = 0
    area_list = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                cnt += 1
                area = 0
                dfs(graph, (x, y))
                area_list.append(area)
    print(cnt)
    print(' '.join(str(_) for _ in sorted(area_list)))
