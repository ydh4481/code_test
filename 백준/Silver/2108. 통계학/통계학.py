import sys
from collections import Counter

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    numbers = []

    for _ in range(n):
        numbers.append(int(input()))

    counter = Counter(numbers)
    mode = sorted(counter.items(), key=lambda x: (x[1], -x[0]), reverse=True)

    if len(mode) > 1:
        if mode[0][1] == mode[1][1]:
            mode = mode[1][0]
        else:
            mode = mode[0][0]
    else:
        mode = mode[0][0]

    print(round(sum(numbers) / n))
    print(sorted(numbers)[len(numbers) // 2])
    print(mode)
    print(max(numbers) - min(numbers))

