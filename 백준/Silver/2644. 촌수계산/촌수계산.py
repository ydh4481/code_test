from collections import defaultdict, deque


def bfs(graph, start_node, target_node):
    queue = deque([(start_node, 0)])  # (current node, current depth)
    visited = set()

    while queue:
        curr_node, depth = queue.popleft()
        if curr_node == target_node:
            return depth
        if curr_node not in visited:
            visited.add(curr_node)
            for next_node in graph[curr_node]:
                if next_node not in visited:
                    queue.append((next_node, depth + 1))
    return -1


if __name__ == '__main__':
    n = int(input())
    start, target = map(int, input().split())
    m = int(input())

    graph = defaultdict(list)

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    print(bfs(graph, start, target))
