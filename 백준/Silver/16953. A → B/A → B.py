from collections import deque


def bfs(start, target):
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        curr, cnt = queue.popleft()

        if curr == target:
            return cnt + 1
        if curr > target:
            continue

        for n in [curr * 2, int(str(curr) + '1')]:
            if n not in visited and n <= target:
                queue.append((n, cnt + 1))
                visited.add(n)
    return -1


if __name__ == '__main__':
    a, b = map(int, input().split())

    print(bfs(a, b))
