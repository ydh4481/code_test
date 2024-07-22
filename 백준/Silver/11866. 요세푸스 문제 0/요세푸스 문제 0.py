if __name__ == '__main__':
    n, k = map(int, input().split())

    mans = [n for n in range(1, n + 1)]
    target = 0
    result = []

    for _ in range(n):
        target += k - 1
        if target >= len(mans):
            target %= len(mans)

        result.append(str(mans.pop(target)))

    print(f"<{', '.join(result)}>")

