n, m, k = list(map(int, input().split()))

numbers = []
for _ in range(n):
    numbers.append(list(map(int, input().split())))

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * m for _ in range(n)]
answer = -1000000


def dfs(x, y, cnt, _sum):
    global answer
    if cnt == k:
        answer = max(answer, _sum)
        return

    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if visited[i][j]: continue

            for dx, dy in directions:
                _x, _y = i + dx, j + dy

                if 0 <= _x < n and 0 <= _y < m and visited[_x][_y]:
                    break
            else:
                visited[i][j] = True
                dfs(i, j, cnt + 1, _sum + numbers[i][j])
                visited[i][j] = False


dfs(0, 0, 0, 0)
print(answer)
