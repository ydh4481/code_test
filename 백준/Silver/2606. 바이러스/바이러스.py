from collections import defaultdict, deque


def bfs(graph, start_node):
    queue = deque([start_node])
    visited = [start_node]

    while queue:
        curr_node = queue.popleft()

        for next_node in graph[curr_node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.append(next_node)

    return visited


if __name__ == '__main__':
    computers = int(input())
    edges = int(input())
    graph = defaultdict(list)

    for i in range(edges):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    print(len(bfs(graph, 1)) - 1)
