if __name__ == '__main__':
    n = int(input())

    times = sorted(list(map(int, input().split())))

    result = 0
    total = 0
    for t in times:
        result += t
        total += result
    print(total)
