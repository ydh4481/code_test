from collections import deque


def bfs(start, end):
    line = [0] * 100001
    queue = deque([start])

    while queue:
        x = queue.popleft()

        if x == end:
            return line[x]

        for next_x in [x + 1, x - 1, x * 2]:
            if 0 <= next_x < 100001 and not line[next_x]:
                line[next_x] = line[x] + 1
                queue.append(next_x)


if __name__ == '__main__':
    n, k = map(int, input().split())

    answer = bfs(n, k)
    print(answer)
