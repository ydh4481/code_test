from collections import defaultdict, deque


def dfs(graph, start_node, visited=[]):
    visited.append(start_node)

    for next_node in sorted(graph[start_node]):
        if next_node not in visited:
            dfs(graph, next_node, visited)

    return [str(_) for _ in visited]


def bfs(graph, start_node):
    queue = deque([start_node])
    visited = [start_node]

    while queue:
        curr_node = queue.popleft()

        for next_node in sorted(graph[curr_node]):
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
    return [str(_) for _ in visited]


if __name__ == '__main__':
    n, m, v = map(int, input().split())
    
    graph = defaultdict(list)
    
    for i in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    
    print(' '.join(dfs(graph, v)))
    print(' '.join(bfs(graph, v)))
