if __name__ == '__main__':
    paper = [[0 for j in range(100)] for i in range(100)]

    n = int(input())

    for _ in range(n):
        y, x = map(int, input().split())
        x = 99 - x - 10

        for i in range(x, x + 10):
            for j in range(y, y + 10):
                paper[i][j] = 1

    print(sum([sum(_) for _ in paper]))
