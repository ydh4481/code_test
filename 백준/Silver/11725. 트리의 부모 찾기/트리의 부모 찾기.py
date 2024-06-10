import sys
from collections import defaultdict, deque


def bfs(graph, start_node):
    queue = deque([start_node])
    visited = [0] * (len(graph) + 1)

    tree = defaultdict()
    while queue:
        curr_node = queue.popleft()
        for next_node in graph[curr_node]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)
                tree[next_node] = curr_node

    return tree


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    graph = defaultdict(list)
    for _ in range(n - 1):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)

    tree = bfs(graph, 1)

    for i in range(2, n + 1):
        print(tree[i])
