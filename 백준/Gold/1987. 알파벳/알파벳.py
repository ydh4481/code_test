def dfs(graph, start, visited=None):
    if visited is None:
        visited = {graph[start[0]][start[1]]}
    global answer
    answer = max(answer, len(visited))

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = start[0] + dx, start[1] + dy
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if graph[nx][ny] not in visited:
                visited.add(graph[nx][ny])
                visited = dfs(graph, (nx, ny), visited)
                visited.remove(graph[nx][ny])

    return visited


if __name__ == '__main__':
    r, c = map(int, input().split())

    graph = []
    for _ in range(r):
        graph.append(list(input()))
    answer = 0
    dfs(graph, (0, 0))
    print(answer)
