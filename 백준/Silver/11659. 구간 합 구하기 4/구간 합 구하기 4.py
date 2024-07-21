import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())

    numbers = list(map(int, input().split()))
    cumsum = [0] * (n + 1)

    for i in range(1, n + 1):
        cumsum[i] = cumsum[i - 1] + numbers[i - 1]

    for _ in range(m):
        i, j = map(int, input().split())
        print(cumsum[j] - cumsum[i - 1])
