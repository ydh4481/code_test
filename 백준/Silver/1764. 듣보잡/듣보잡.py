from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())

    names = defaultdict(int)

    for _ in range(n + m):
        names[input()] += 1

    result = []
    total = 0
    for name, cnt in names.items():
        if cnt == 2:
            result.append(name)
            total += 1

    print(total)
    for name in sorted(result):
        print(name)
