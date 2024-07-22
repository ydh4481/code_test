import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    nodes = []

    for _ in range(n):
        nodes.append(tuple(map(int, input().split())))

    for x, y in sorted(nodes, key=lambda x: (x[1], x[0])):
        print(x, y)
