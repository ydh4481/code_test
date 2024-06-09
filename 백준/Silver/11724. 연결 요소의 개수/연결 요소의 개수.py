from collections import defaultdict, deque


def bfs(graph, start, visited):
    queue = deque([start])

    while queue:
        curr_node = queue.popleft()
        for next_node in graph[curr_node]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)

    return visited


if __name__ == '__main__':
    import sys

    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0] * (n + 1)

    cnt = 0
    for key in range(1, n + 1):
        if not visited[key]:
            cnt += 1
            visited = bfs(graph, key, visited)

    print(cnt)
